from uuid import uuid4 
from .item import Item

class Electronics(Item): # Updated class to inherit from Item
    def __init__(self, id=None, type="Unknown", condition=0):
        self.id = uuid4().int if id is None else id
        self.type = "Unknown" if type == "Unknown" else type
        super().__init__(id=id, condition=condition)  # pass condition to Item

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}."\
            f" This is a {self.type} device."