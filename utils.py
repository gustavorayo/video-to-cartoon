import time
import os
import cv2


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        formatted_time = "{:.6f}".format(elapsed_time)
        print(f"Time taken by {func.__name__}: {formatted_time} seconds")
        return result

    return wrapper


class VideoParser:
    def __init__(self, video_origin, frames_destination, clean_folder=False):
        self.video_path = video_origin
        self.frame_path = frames_destination
        self.frame_limit = 120
        self.img_size = 512
        if clean_folder and os.path.exists(self.frame_path):
            self.clean_folder()

        # Taken from https://medium.com/curious-manava/center-crop-and-scaling-in-opencv-using-python-279c1bb77c74

    def center_crop(self, img, dim):
        """Returns center cropped image
    Args:
    img: image to be center cropped
    dim: dimensions (width, height) to be cropped
    """
        width, height = img.shape[1], img.shape[0]

        # process crop width and height for max available dimension
        crop_width = dim[0] if dim[0] < img.shape[1] else img.shape[1]
        crop_height = dim[1] if dim[1] < img.shape[0] else img.shape[0]
        mid_x, mid_y = int(width / 2), int(height / 2)
        cw2, ch2 = int(crop_width / 2), int(crop_height / 2)
        crop_img = img[mid_y - ch2:mid_y + ch2, mid_x - cw2:mid_x + cw2]
        return crop_img

    def clean_folder(self):
        for filename in os.listdir(self.frame_path):
            os.remove(os.path.join(self.frame_path, filename))

    @timing_decorator
    def video_to_frames(self):
        output_directory = self.frame_path
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        cap = cv2.VideoCapture(self.video_path)
        frame_count = 0

        ret, frame = cap.read()
        if not ret:
            print("Error reading frame.")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_count += 1
            frame_filename = f'{frame_count:04d}.jpg'
            frame_path = os.path.join(output_directory, frame_filename)
            img = self.center_crop(frame, (self.img_size, self.img_size))
            cv2.imwrite(frame_path, img)
            if frame_count == self.frame_limit:
                break

        cap.release()
