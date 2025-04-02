### WAVE 5

from uuid import uuid4 

class Decor:
    def __init__(self, id=None, width=0, length=0):
        self.id = uuid4().int if id is None else id
        self.width = 0 if width == 0 else width
        self.length = 0 if length == 0 else length

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Decor with id {self.id}."\
            f" It takes up a {self.width} by {self.length} sized space."

