
from typing import List

from typing import List

class Node:
    def __init__(self, function:object, function_name:str, arguments:List=[])->None:
        self.function = function
        self.function_name:str = function_name
        self.params:List = arguments
        self.next:str = None
