from uuid import uuid4 

class Electronics:
    def __init__(self, id=None, type="Unknown"):
        self.id = uuid4().int if id is None else id
        self.type = "Unknown" if type == "Unknown" else type

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}."\
            f" This is a {self.type} device."