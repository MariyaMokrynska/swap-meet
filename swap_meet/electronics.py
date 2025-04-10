from .item import Item

class Electronics(Item): # Updated class to inherit from Item
    def __init__(self, id=None, type="Unknown", condition=0):
        self.type = "Unknown" if type == "Unknown" else type
        super().__init__(id, condition)  # pass condition to Item

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}."\
            f" This is a {self.type} device."