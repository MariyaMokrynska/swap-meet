from uuid import uuid4 
from .item import Item

class Clothing(Item): # Updated class to inherit from Item
    def __init__(self, id=None, fabric="Unknown", condition=0):
        self.id = uuid4().int if id is None else id
        self.fabric = fabric if fabric != "Unknown" else "Unknown"
        super().__init__(id, condition)  # pass condition to Item

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}."\
        f" It is made from {self.fabric} fabric."


