from uuid import uuid4 

class Clothing: 
    def __init__(self, id=None, fabric="Unknown"):
        self.id = uuid4().int if id is None else id
        self.fabric = fabric if fabric != "Unknown" else "Unknown"

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}."\
        f" It is made from {self.fabric} fabric."
    
item_a = Clothing(123435, "Wool")
print(str(item_a))