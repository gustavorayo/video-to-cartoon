import time
import os
import cv2
from PIL import Image
import numpy as np


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


class Grid:
    def __init__(self, grid_size):
        self.grid_size = grid_size

    def get_image(self, image):
        return Image.open(image) if isinstance(image, str) else image

    def merge_images(self, images):
        rows, cols = self.grid_size
        first_image = self.get_image(images[0])
        img_width, img_height = first_image.size

        # Create an empty canvas for the grid
        grid = np.zeros((img_height * rows, img_width * cols, 3), dtype=np.uint8)

        # Loop through the images and place them in the grid
        for i in range(rows):
            for j in range(cols):
                index = i * cols + j
                if index < len(images):
                    img = np.array(self.get_image(images[index]))
                    grid[i * img_height:(i + 1) * img_height, j * img_width:(j + 1) * img_width, :] = img

        return Image.fromarray(grid)

    def split_images(self, img):
        rows, cols = self.grid_size
        # Get the height and width of each individual image
        img_width, img_height = img.size
        img_width = int(img_width / cols)
        img_height = int(img_height / rows)
        combined_image = np.array(img)
        individual_images = []

        # Split the combined image into individual images
        for i in range(rows):
            for j in range(cols):
                start_x = j * img_width
                end_x = (j + 1) * img_width
                start_y = i * img_height
                end_y = (i + 1) * img_height

                individual_image = combined_image[start_y:end_y, start_x:end_x, :]
                individual_images.append(individual_image)
        return individual_images
