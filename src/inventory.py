import pathlib
import sys

CUR_FOLDDER = str(pathlib.Path(__file__).parent.resolve()) 
PATH = (CUR_FOLDDER + "\Entities")
'''
Get the current path of the folder contains this file Path.(__file__)
and make it become an abs path
'''

sys.path.append(PATH)

from Entities.item import Item

class Inventory:
    def __init__(self, capcity):
        self.capcity = capcity


