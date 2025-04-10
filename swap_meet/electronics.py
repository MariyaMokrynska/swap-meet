from .item import Item

class Electronics(Item): # Updated class to inherit from Item
    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id, condition)  # pass id and condition to Item, move 
                                        # the line above child's custom attribute
        self.type = "Unknown" if type == "Unknown" else type
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}."\
            f" This is a {self.type} device."