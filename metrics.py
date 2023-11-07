import torch
from transformers import CLIPImageProcessor, CLIPModel, CLIPTokenizer
from PIL import Image
from utils import timing_decorator
import os

# Load the CLIP model
model_ID = "openai/clip-vit-base-patch32"
model = CLIPModel.from_pretrained(model_ID)

preprocess = CLIPImageProcessor.from_pretrained(model_ID)


def load_and_preprocess_image(image_path):
    image = Image.open(image_path)
    image = preprocess(image, return_tensors="pt")
    return image


@timing_decorator
def compute_clip_score(frames_destination, extension="png"):
    generated_files = [os.path.join(frames_destination, f) for f in os.listdir(frames_destination) if
                       f.endswith(extension)]
    generated_files = sorted(generated_files)
    print(generated_files)
    start = 0
    scores = []
    for i in generated_files[1:]:
        image_a = load_and_preprocess_image(generated_files[start])["pixel_values"]
        image_b = load_and_preprocess_image(i)["pixel_values"]
        start = start + 1
        with torch.no_grad():
            embedding_a = model.get_image_features(image_a)
            embedding_b = model.get_image_features(image_b)
        similarity_score = torch.nn.functional.cosine_similarity(embedding_a, embedding_b)
        scores.append(similarity_score.item())
    return scores
