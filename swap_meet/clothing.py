from .item import Item

class Clothing(Item): # Updated class to inherit from Item
    def __init__(self, id=None, fabric="Unknown", condition=0):
        super().__init__(id, condition)  # pass id and condition to parent constructor, 
                                        # move the line above child's custom attribute
        self.fabric = fabric if fabric != "Unknown" else "Unknown"
    
    def __str__(self):
        return f"{super().__str__()} It is made from {self.fabric} fabric."


