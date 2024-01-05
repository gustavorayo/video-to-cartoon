import os
from subprocess import PIPE, run
from utils import timing_decorator


class StylePropagator:
    def __init__(self, video_destination, key_frames, original_frames,
                 frames_destination, fps=30, patch_number=5, frame_extension="png"):
        self.video_destination = video_destination
        self.frames_destination = frames_destination
        self.key_frames = key_frames
        self.patch_number = patch_number
        self.original_frames = original_frames
        self.create_folder(video_destination)
        self.fps = fps
        self.frame_extensions = frame_extension

    def create_folder(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def get_guide(self, o, d):
        source_path = self.original_frames
        source_guide = source_path + f"/{o:04d}.{self.frame_extensions}"
        target_guide = source_path + f"/{d:04d}.{self.frame_extensions}"
        guide = f"-guide {source_guide} {target_guide} -weight 4"
        return guide

    def set_style(self, s, o, d, inlcude_prev=False):
        style = self.key_frames + f"/{s:04d}.{self.frame_extensions}"
        guide = self.get_guide(o, d)
        output = os.path.join(self.frames_destination, f"{d:04d}.{self.frame_extensions}")
        command = f"{self.ebsynth_path} -style {style} {guide} -output {output}"
        print(command)
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
        print(result.stdout)

    def generate_left(self, p, length):
        for i in range(p - length, p):
            self.set_style(p, p, i)

    def generate_right(self, p, length):
        for i in range(p, p + length):
            self.set_style(p, p, i)

    def apply_style(self, start, end, interval):
        key_start = int(interval / 2)
        for key_frame_index in range(key_start, end + 1, interval):
            print(f"==={key_frame_index}===")
            # lframes = self.patch_number-1 # 1..5
            # rframes = self.patch_number+1 # 6..10
            lframes = key_start - 1  # 1..5
            rframes = key_start + 1  # 6..10
            self.generate_left(key_frame_index, lframes)
            self.generate_right(key_frame_index, rframes)

    def propagate_style(self, start, end, interval):
        if not os.path.exists(self.frames_destination):
            os.makedirs(self.frames_destination)
        self.apply_style(start, end, interval)

    @timing_decorator
    def get_ebsynth(self, oring_folder, ebsynth_dest):
        ebsynth_origin = os.path.join(oring_folder, 'ebsynth')
        self.ebsynth_path = os.path.join(ebsynth_dest, "ebsynth")
        self.create_folder(ebsynth_dest)
        if not os.path.exists(self.ebsynth_path):
            command = f"cp {ebsynth_origin} {ebsynth_dest}"
            result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
            print(result.stdout)
            result = run(f"chmod +x {self.ebsynth_path}", stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
            print(result.stdout)

    def generate_video(self, output_name):
        result_video_name = os.path.join(self.video_destination, output_name)
        # !(cd $self.frames_destination && ffmpeg -framerate 30 -pattern_type glob -i '*.png' -c:v libx264 -pix_fmt yuv420p $result_video_name)

    @timing_decorator
    def basic_propagation(self, ebsynth_folder, ebsynth_dest, output_name, start=1, end=120, interval=10):
        result_video_name = os.path.join(self.video_destination, output_name)
        if os.path.exists(result_video_name):
            print("Video already exist", result_video_name)
            return
        self.get_ebsynth(ebsynth_folder, ebsynth_dest)
        self.propagate_style(start, end, interval)
        self.generate_video(output_name)

    @timing_decorator
    def advanced_propagation(self, ebsynth_folder, output_name, video_root_folder, end=120, interval=10, proc=4):
        ebsynth_dest = 'deps/Rerender_A_Video/deps/ebsynth/bin/'
        self.get_ebsynth(ebsynth_folder, ebsynth_dest)
        self.create_folder(video_root_folder)
        keys = os.path.join(video_root_folder, "keys")
        video = os.path.join(video_root_folder, "video")
        destination = os.path.join(self.video_destination, output_name)
        self.create_folder(keys)
        self.create_folder(video)
        run(f"cp {self.key_frames}/* {keys}", stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
        run(f"cp {self.original_frames}/* {video}", stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
        command = f"cd deps/Rerender_A_Video && python video_blend.py {video_root_folder} --end {end} --itv {interval} --key keys --output {destination} --fps {self.fps} --n_proc {proc}"
        print(command)
        r = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
        print(r.stdout, r.stderr)
