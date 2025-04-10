### WAVE 5
from .item import Item

class Decor(Item): # Updated class to inherit from Item
    def __init__(self, id=None, width=0, length=0, condition=0):
        super().__init__(id, condition)  # pass id and condition to Item, move 
                                        # the line above child's custom attribute
        self.width = 0 if width == 0 else width
        self.length = 0 if length == 0 else length
    
    def __str__(self):
        return f"An object of type Decor with id {self.id}."\
            f" It takes up a {self.width} by {self.length} sized space."

