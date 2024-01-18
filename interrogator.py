from clip_interrogator import Config, Interrogator


class ClipInterrogator():
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
