import argparse
import os
from  style_propagator import StylePropagator
from  keyframe_generator import KeyFramesGenerator
def main(args):
    style = args.style
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
    keyframes= "tmp/keyframes"
    propagated_frames = 'tmp/propagated'
    os.makedirs(frames, exist_ok=True)
    os.makedirs(keyframes, exist_ok=True)

    os.makedirs(keyframes, exist_ok=True)
    kfgen = KeyFramesGenerator(frames, keyframes, keword_only=False, interval=30, start=1, difussion_configs=configs)
    kfgen.generate_key_frames(grid=True)
    video_path = "tmp/video"
    st = StylePropagator(video_path, keyframes, frames, propagated_frames)
    local_ebsynth_path = "bin/ebsynth"
    ebsynth_temp = "tmp/ebsynth_temp"
    st.advanced_propagation(local_ebsynth_path, args.output, ebsynth_temp, end=120, interval=30)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_video', type=str, help='Path to input video')
    parser.add_argument('--output',
                        type=str,
                        default=None,
                        help='Path to output video')
    parser.add_argument('--style',
                        type=str,
                        default=None,
                        help='Path to output video')
    args = parser.parse_args()
    main(args)
