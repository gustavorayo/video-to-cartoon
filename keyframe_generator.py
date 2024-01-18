import os
from PIL import Image

from controlnet_aux import HEDdetector
from utils import timing_decorator, Grid
from interrogator import ClipInterrogator
from image_converter import ImageConverter


class KeyFramesGenerator:
    def __init__(self, frames_origin,
                 frames_destination, keword_only=True, limit=120, interval=10, start=5, prompts=None,
                 frame_extension="png", difussion_configs={}):
        self.frames_destination = frames_destination
        self.img_text_method = 'fast'
        self.difussion_configs = difussion_configs
        self.frames_origin = frames_origin
        self.limit = limit
        self.interval = interval
        self.keword_only = keword_only
        self.pipeline_type = difussion_configs['pipeline_type']
        self.set_pipeline(difussion_configs)
        self.set_detector()
        self.grid_size = 4
        self.grid = Grid((2, 2))
        self.start = start
        self.prompts = prompts
        self.frame_extension = frame_extension
        if (not self.keword_only) and prompts == None:
            print("Loading clip")
            self.clipInt = ClipInterrogator()
            self.clipInt.load_interrogator()

    def set_pipeline(self, difussion_configs):
        self.ic = ImageConverter(low_cpu_mem_usage=True)
        model_id, keyword = self.ic.get_model(difussion_configs["style"])
        print("model and style", model_id, keyword)
        self.keyword = keyword
        self.ic.load(difussion_configs['pipeline_type'], model_id, controlnets=difussion_configs['controlnets'])

    def save_images(self, imgs, names):
        path = self.frames_destination
        self.create_foler(path)
        for i, img in enumerate(imgs):
            file_name = f'{path}/{names[i]}'
            image = Image.fromarray(img)
            image.save(file_name)

    def set_detector(self):
        pipeline_type = self.pipeline_type
        if pipeline_type == "Controlnet_text2img" or pipeline_type == "Controlnet_img2img":
            self.hed = HEDdetector.from_pretrained("lllyasviel/Annotators")

    def create_foler(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def get_key_files(self):
        names = []
        paths = []
        start = self.start
        for i in range(start, self.limit + 1, self.interval):
            file_name = f'{i:04d}.{self.frame_extension}'
            file_path = os.path.join(self.frames_origin, file_name)
            names.append(file_name)
            paths.append(file_path)
        return names, paths

    @timing_decorator
    def generate_key_frames(self, grid=True):
        if grid:
            self.generate_keyframes_from_grid()
        else:
            self.generate_independent_frames()

    def generate_keyframes_from_grid(self):
        names, paths = self.get_key_files()
        samples = []
        grid_names = []
        prompt_index = 1
        for i in range(1, len(names) + 1):
            file_name = names[i - 1]
            file_path = paths[i - 1]
            samples.append(file_path)
            grid_names.append(file_name)
            ## generate one image per grid size
            if i % self.grid_size == 0:
                dest_path = os.path.join(self.frames_destination, file_name)
                if not os.path.exists(dest_path):
                    # Could use first frame instead of last or even one from the middle. samples[0]
                    # what about all?
                    prompt = self.get_prompt(Image.open(file_path), prompt_index)  # use last image for prompt
                    print("generating:", grid_names)
                    rs_image = self.grid.merge_images(samples)
                    cartoonized_image = self.convert_image(prompt, rs_image, self.difussion_configs)
                    imgs = self.grid.split_images(cartoonized_image)
                    self.save_images(imgs, grid_names)
                samples = []
                grid_names = []
                prompt_index = prompt_index + 1

    def generate_independent_frames(self):
        names, paths = self.get_key_files()
        path = self.frames_destination
        self.create_foler(path)
        for i in range(1, len(names) + 1):
            file_name = names[i - 1]
            file_path = paths[i - 1]
            dest_path = os.path.join(path, file_name)
            if os.path.exists(dest_path):
                continue

            print("generating:", dest_path)
            img = Image.open(file_path)
            prompt = self.get_prompt(img)  # use last image for prompt
            cartoonized_image = self.convert_image(prompt, img, self.difussion_configs)
            cartoonized_image.save(dest_path)

    def get_prompt(self, img, index=None):
        style_key_word = self.keyword
        if self.keword_only:
            prompt = f"{style_key_word}"
        else:
            if self.prompts == None:
                text = self.clipInt.image_to_prompt(img, self.img_text_method)
                prompt = f"{style_key_word}, {text}"
            else:
                prompt = f"{style_key_word}, {self.prompts[index]}"
        return prompt

    def convert_image(self, prompt, rs_image, df):
        if self.pipeline_type == 'img2img':
            cartoonized_image = self.ic.img2img(prompt, rs_image, df["strength"])

        if self.pipeline_type == 'Controlnet_text2img':
            first_control = self.canny(rs_image)
            cartoonized_image = self.ic.text_to_image(prompt,
                                                      control_images=[first_control],
                                                      controlnet_conditioning_scale=df["controlnet_conditioning_scale"],
                                                      control_guidance_end=df["control_guidance_end"],
                                                      negative_prompt=df["negative_prompt"])

        if self.pipeline_type == 'Controlnet_img2img':
            size = rs_image.size[0]
            first_control = self.hed(rs_image, detect_resolution=size, image_resolution=size)
            cartoonized_image = self.ic.controlled_img2img(prompt, rs_image, df["strength"],
                                                           control_images=[first_control],
                                                           num_inference_steps=df["num_inference_steps"],
                                                           controlnet_conditioning_scale=df[
                                                               "controlnet_conditioning_scale"],
                                                           control_guidance_end=df["control_guidance_end"],
                                                           negative_prompt=df["negative_prompt"])
        return cartoonized_image
