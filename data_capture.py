import cv2
import os

from PIL import Image
from pathlib import Path


class ImageProcessor:
    def __init__(self, data_folder):
        self.data_folder = data_folder

    def capture_image(self):
        cap = cv2.VideoCapture(0)
        _, image = cap.read()
        cap.release()
        return image

    def process_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(image)
        return img

    def save_image(self, img):
        files = os.listdir(self.data_folder)
        img.save(Path.joinpath(self.data_folder, f'img {len(files)}.png'))

    def process_and_save_image(self):
        image = self.capture_image()
        processed_img = self.process_image(image)
        self.save_image(processed_img)


data_folder = Path(os.getcwd()) / 'data'

processor = ImageProcessor(data_folder)

user_input = ""

while user_input.lower() not in ["q"]:
    processor.process_and_save_image()
    user_input = input("Press q to quit or any other key to continue: ")




