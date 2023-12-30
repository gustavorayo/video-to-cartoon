import argparse
import os
from style_propagator import StylePropagator
from keyframe_generator import KeyFramesGenerator
from utils import VideoParser

def main(style, video_name, video_length=91):
    # style = args.style
    configs = {
        "pipeline_type": "Controlnet_img2img",
        "style": style,
        "scheduler": "Euler a",
        "negative_prompt": None,
        "strength": 0.6,
        "controlnets": ["lllyasviel/sd-controlnet-hed"],
        "controlnet_conditioning_scale": [0.7],
        "control_guidance_end": [0.8],
        "num_inference_steps": 25
    }
    frames = "tmp/frames"
    keyframes = "tmp/keyframes"
    propagated_frames = 'tmp/propagated'
    os.makedirs(frames, exist_ok=True)
    os.makedirs(keyframes, exist_ok=True)

    sections = 3
    interval = int((video_length - 1) / sections)
    processable_length = ((interval * sections) + 1)

    video_file = f'01.mp4'
    video_path = os.path.join("./dataset", video_file)
    vp = VideoParser(video_path, frames, frame_limit=processable_length, clean_folder=True)
    vp.video_to_frames(frame_extension="png")
    os.makedirs(keyframes, exist_ok=True)
    kfgen = KeyFramesGenerator(frames, keyframes, keword_only=False, interval=interval, start=1,
                               frame_extension="png",
                               difussion_configs=configs)
    kfgen.generate_key_frames(grid=True)
    video_path = "tmp/video"
    st = StylePropagator(video_path, keyframes, frames, propagated_frames)
    local_ebsynth_path = "bin/ebsynth"
    ebsynth_temp = "tmp/"
    st.advanced_propagation(local_ebsynth_path, video_name, ebsynth_temp, end=processable_length, interval=interval)

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--input_video', type=str, help='Path to input video')
#     parser.add_argument('--output',
#                         type=str,
#                         default=None,
#                         help='Path to output video')
#     parser.add_argument('--style',
#                         type=str,
#                         default=None,
#                         help='Path to output video')
#     args = parser.parse_args()
#     main(args['style'], args['output'])
