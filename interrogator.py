import os
from PIL import Image

from clip_interrogator import Config, Interrogator
class ClipInterrogator():
  # def get_prompts(self, interval, limit):
  #   prompts = {}
  #   prompts_list = []
  #   for i in range(1, self.limit+1, self.clip_interval):
  #     file_name = f"{i:04d}.jpg"
  #     file_path = os.path.join(self.frames_origin, file_name)
  #     prompts[file_name] =  self.image_to_prompt(Image.open(file_path), self.img_text_method)
  #     prompts_list.append(prompts[file_name])
  #   return prompts, prompts_list

  def load_interrogator(self):
    config = Config()
    config.clip_model_name = 'ViT-L-14/openai'
    config.caption_model_name = 'blip-large'
    self.ci = Interrogator(config)

  def image_to_prompt(self, image, mode):
    image = image.convert('RGB')
    ci = self.ci
    if mode == 'best':
        return ci.interrogate(image)
    elif mode == 'classic':
        return ci.interrogate_classic(image)
    elif mode == 'fast':
        return ci.interrogate_fast(image)
    elif mode == 'negative':
        return ci.interrogate_negative(image)