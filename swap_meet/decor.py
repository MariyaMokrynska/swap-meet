# WAVE 5
from .item import Item


class Decor(Item):  # Updated class to inherit from Item
    def __init__(self, id=None, width=0, length=0, condition=0):
        super().__init__(id, condition)  # pass id and condition to Item, move
        # the line above child's custom attribute
        # self.width = 0 if width == 0 else width
        # self.length = 0 if length == 0 else length
        self.width = width if width else 0
        self.length = length if length else 0

    def __str__(self):
        return f"{super().__str__()} It takes up a {self.width} by "\
            f"{self.length} sized space."
