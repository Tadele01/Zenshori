from pathlib import Path
from distutils.dir_util import copy_tree
from image import ImageProcessor
from node import Node
from typing import  Dict

import os
import shutil



class Zenshori:
    def __init__(self, folder_name:str, dest=None)->None:
        '''
            Base class 
            
            params:
                folder_name : A folder path 
                dest : A folder where the new preprocessed images will be saved 
                            if not given it takes pythons's cwd

            
        '''
        self.folder:str = folder_name
        self.new_folder:str = 'preprocessed_' + self.folder
        self.image_processor:object = None
        self.graph = None

        if dest:
            self.new_folder:str = dest + '/' + self.new_folder
        
        try:
            copy_tree(self.folder, self.new_folder)
        except Exception as exp:
            print(exp)     
            return None

        # self.image_processor = ImageProcessor(self.new_folder)

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


        
    
    def inspect(self):
        head = self.graph
        while head != None:
            print(head.function_name, head.params)
            for val in head.params:
                print(head.function(val))
            head = head.next





zen = Zenshori('trial')
import math
zen.pipeline({abs:[1, 2, 3] , math.ceil:[12, 13, 14]})








    
    





