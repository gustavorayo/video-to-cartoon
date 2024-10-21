import argparse
import os
from style_propagator import StylePropagator
from keyframe_generator import KeyFramesGenerator
from utils import VideoParser
import cv2


def count_frames(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file")
        return -1

    # Get the total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    cap.release()

    return total_frames


def main(source_video, style, output_video_name="test.mp4", video_length=None):
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

    if video_length is None:
        video_length = count_frames(source_video)

    current_path = os.getcwd()
    frames = current_path + "/tmp/frames"
    keyframes = current_path + "/tmp/keyframes"
    propagated_frames = current_path + '/tmp/propagated'
    os.makedirs(frames, exist_ok=True)
    os.makedirs(keyframes, exist_ok=True)

    sections = 3
    interval = int((video_length - 1) / sections)
    processable_length = ((interval * sections) + 1)
    print("Number of frames:", processable_length)

    vp = VideoParser(source_video, frames, frame_limit=processable_length, clean_folder=True)
    vp.video_to_frames(frame_extension="png")
    os.makedirs(keyframes, exist_ok=True)
    kfgen = KeyFramesGenerator(frames, keyframes, keword_only=False, limit=processable_length, interval=interval, start=1,
                               frame_extension="png",
                               difussion_configs=configs)
    kfgen.generate_key_frames(grid=True)
    video_path = current_path  # output video folder. Current folder.
    st = StylePropagator(video_path, keyframes, frames, propagated_frames)
    local_ebsynth_path = "bin"
    video_root_folder = current_path + "/tmp"  # temporal directory for intermediate files
    st.advanced_propagation(local_ebsynth_path, output_video_name, video_root_folder, end=processable_length,
                            interval=interval)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_video', type=str, help='Path to input video')
    parser.add_argument('--output',
                        type=str,
                        default='test.mp4',
                        help='Path to output video')
    parser.add_argument('--style',
                        type=str,
                        default=None,
                        help='Path to output video')
    parser.add_argument('--frames',
                        type=int,
                        default=None,
                        help='Number of frames to translate')
    args = parser.parse_args()
    main(args.input_video, args.style, args.output, args.frames)
