from pathlib import Path
import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, folder:str)->None:
        self.folder:str = folder
        self.images:'generator' = self.load_images()

    def load_images(self)->'generator':
        data_dir:str = Path(self.folder)
        all_images:'generator' = data_dir.glob('**/*.jpg')

        return all_images

    

    

    

    

img = ImageProcessor('Fundus_Train_Val_Data')

print(type(img.load_images()))


