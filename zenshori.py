from pathlib import Path
from distutils.dir_util import copy_tree
from image import ImageProcessor
from node import Node
from typing import  Dict, List
from errors import NoPipeline, NoImageDirectory

import os
import shutil



class Zenshori:
    def __init__(self, folder_name:str, dest:str=None)->None:
        '''
            Base class 
            
            params:
                folder_name : A folder path 
                dest : A folder where the new processed images will be saved 
                            if not given it takes cwd

            
        '''
        self.folder:str = folder_name
        self.images_folder:str = 'preprocessed_' + self.folder
        self.image_processor:object = None
        self.graph:List[Node] = None
        self.images = None

        if dest:
            self.images_folder = dest + '/' + self.images_folder
        
        try:
            copy_tree(self.folder, self.images_folder)
            self.images = ImageProcessor(self.images_folder).load_images()
        except Exception as exp:
            print(exp)     
            return None
        

    def pipeline(self, functions:Dict)->None:
        cur_node:Node = self.graph
        i:int = 0
        for function, args in functions.items():
            if i == 0:
                function_name = function.__name__
                self.graph = Node(function, function_name, args)
                cur_node, i = self.graph, i+1
                continue
            function_name = function.__name__
            node = Node(function, function_name, args)
            cur_node.next = node
            cur_node = node

    def processs_images(self)-> str:
        if self.images and self.graph:
            ImageProcessor.processor(self.images, self.graph)
            return self.images_folder
        else:
            if not self.images:
                print('No images directory provided')
                raise NoImageDirectory
            if not self.images:
                print('No processing pipline provided')
                raise NoPipeline
            
    def inspect(self):
        print("Preprocessing Steps")
        separator:str = "====================================================================="
        table:str = '---------------------------------------------------------------------'
        print(table)
        print('{0: <40}'.format("Processing functions"), "Parameters", sep='')
        print(table)
        head:Node = self.graph
        while head:
            print('{0: <40}'.format(head.function_name), end='')
            print(head.params, sep='\n')
            head = head.next
            print(separator)
        print(table)
            
        




zen = Zenshori('trial')
import math
zen.pipeline({abs:[1, 2, 3] , math.ceil:[12, 13, 14]})

zen.inspect()





    
    





