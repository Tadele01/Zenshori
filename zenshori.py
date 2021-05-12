from pathlib import Path
from distutils.dir_util import copy_tree
import os
import shutil

class Zenshori:
    def __init__(self, folder_name:str, dest=None)->None:
        '''
            Base class 
            
            params:
                folder_path : A folder path 
                save_path : A folder where the new preprocessed images will be saved 
                            if not given it takes pythons's cwd

            
        '''
        self.folder:str = folder_name
        self.new_folder:str = 'preprocessed' + self.folder
        if dest:
            self.new_folder = dest + '/' + self.new_folder
        
        try:
            copy_tree(self.folder, self.new_folder)
        except Exception as exp:
            print(exp)        

    
    





