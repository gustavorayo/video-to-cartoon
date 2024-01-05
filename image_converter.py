import torch
from diffusers import StableDiffusionImg2ImgPipeline, StableDiffusionControlNetImg2ImgPipeline, \
    StableDiffusionControlNetPipeline
from diffusers import EulerAncestralDiscreteScheduler
from diffusers import ControlNetModel
from utils import timing_decorator


class ImageConverter:

    @timing_decorator
    def __init__(self, seed=1234, low_cpu_mem_usage=False):
        self.generator = None
        self.pipeline = None
        self.seed = seed
        self.low_cpu_mem_usage = low_cpu_mem_usage

    @timing_decorator
    def load(self, pipeline_type, model_id, scheduler_name="Euler a", controlnets=None):
        controls = []
        if controlnets:
            for c in controlnets:
                controls.append(ControlNetModel.from_pretrained(c, torch_dtype=torch.float16))

        if scheduler_name == "Euler a":
            scheduler = EulerAncestralDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")

        if pipeline_type == "img2img":
            self.pipeline = StableDiffusionImg2ImgPipeline.from_pretrained(model_id,
                                                                           scheduler=scheduler, safety_checker=None,
                                                                           torch_dtype=torch.float16,
                                                                           low_cpu_mem_usage=self.low_cpu_mem_usage)
        elif pipeline_type == "Controlnet_img2img":
            self.pipeline = StableDiffusionControlNetImg2ImgPipeline.from_pretrained(model_id, scheduler=scheduler,
                                                                                     safety_checker=None,
                                                                                     controlnet=controls,
                                                                                     torch_dtype=torch.float16,
                                                                                     low_cpu_mem_usage=self.low_cpu_mem_usage)
        elif pipeline_type == "Controlnet_text2img":
            self.pipeline = StableDiffusionControlNetPipeline.from_pretrained(model_id, controlnet=controls,
                                                                              safety_checker=None,
                                                                              torch_dtype=torch.float16,
                                                                              low_cpu_mem_usage=self.low_cpu_mem_usage)
        self.generator = torch.Generator(device="cpu").manual_seed(self.seed)
        self.pipeline = self.pipeline.to("cuda")
        self.pipeline.enable_model_cpu_offload()

    def get_model(self, style):
        if style == "Van-Gogh":
            model = "dallinmackay/Van-Gogh-diffusion"
            style_key_word = "lvngvncnt, Van-Gogh"
        elif style == "ghibli":
            model = "nitrosocke/Ghibli-Diffusion"
            style_key_word = "ghibli style"
        elif style == "ryo":
            model = "gustavorayo/ryo-takemasa-v1"
            style_key_word = "ryo takemasa style"
        else:
            raise Exception(f"style {style} not suported")
        return model, style_key_word

    @timing_decorator
    def img2img(self, prompt, reference_image, strength=0.3, num_inference_steps=25, guidance_scale=7):
        images = self.pipeline(prompt=prompt,
                               image=reference_image, strength=strength,
                               num_inference_steps=num_inference_steps, guidance_scale=guidance_scale,
                               generator=self.generator).images
        return images[0]

    @timing_decorator
    def text_to_image(self, prompt, control_images, num_inference_steps=20,
                      controlnet_conditioning_scale=[1.0, 1.0],
                      guidance_scale=7.5, control_guidance_end=[0.5], negative_prompt=None):
        images = self.pipeline(
            prompt,
            image=control_images,
            guidance_scale=guidance_scale,
            negative_prompt=negative_prompt,
            generator=self.generator,
            num_inference_steps=num_inference_steps,
            controlnet_conditioning_scale=controlnet_conditioning_scale,
            control_guidance_end=control_guidance_end
        ).images
        return images[0]

    @timing_decorator
    def controlled_img2img(self, prompt, image, strength=0.5, control_images=[],
                           num_inference_steps=20, guidance_scale=7,
                           controlnet_conditioning_scale=[0.5],
                           control_guidance_end=[0.5], negative_prompt=None):
        print(prompt, image, strength, control_images,
              num_inference_steps, guidance_scale,
              controlnet_conditioning_scale,
              control_guidance_end, negative_prompt)
        images = self.pipeline(
            prompt,
            image=image,
            strength=strength,
            control_image=control_images,
            guidance_scale=guidance_scale,
            negative_prompt=negative_prompt,
            generator=self.generator,
            num_inference_steps=num_inference_steps,
            controlnet_conditioning_scale=controlnet_conditioning_scale,
            control_guidance_end=control_guidance_end
        ).images
        return images[0]
