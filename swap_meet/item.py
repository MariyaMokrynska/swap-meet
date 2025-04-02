import uuid


class Item:
    def __init__(self, id=None):  # default id is None
        """
        Initializes an Item with a unique ID.
        If no ID is provided, a random unique ID is generated using uuid.

        Written By Mariya Mokrynska
        """
        if id == None:
            self.id = uuid.uuid4().int  # unique id
        else:
            self.id = id

    def get_category(self):
        """
        Returns the name of the class as a string.

        Written By Mariya Mokrynska
        """
        return self.__class__.__name__

### WAVE 3 
        
    # Returns a string representation of the Item instance
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    