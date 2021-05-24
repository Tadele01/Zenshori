from node import Node
from pathlib import Path
from typing import List
from node import Node
from PIL import Image

import cv2
import numpy as np


class ImageProcessor:
    def __init__(self, folder:str)->None:
        self.folder:str = folder

    def load_images(self)->'generator':
        data_dir:str = Path(self.folder)
        all_images:'generator' = data_dir.glob('**/*.jpg')

        return all_images

    def processor(self, images:'generator', graph:List[Node]):
        root_node:Node = graph
        for img_path in images:
            img = Image.open(img_path)
            img_matrix = np.asarray(img)
            while graph:
                graph.function(img_matrix, args=graph.args)
                img_matrix = img_matrix.astype(np.uint8)
                img = Image.fromarray(img)
                save_path = str(img_path)
                img.save(save_path)
            
            graph = root_node
        



