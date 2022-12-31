import pathlib
import sys

CUR_FILE = r"C:\Users\ngnhatmih\Desktop\Ouch\Projects\Fantasy-World\src\Entities"
'''
Get the current path of the folder contains this file Path.(__file__)
and make it become an abs path
'''
sys.path.append(CUR_FILE)

from Entities.item import Item

class Inventory:
    def __init__(self, capcity):
        self.capcity = capcity


