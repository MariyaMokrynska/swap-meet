import uuid

# WAVE 2

class Item:
    def __init__(self, id=None, condition=0):  # default id is None
        """
        Initializes an Item with a unique ID.
        If no ID is provided, a random unique ID is generated using uuid.

        Written By Mariya Mokrynska
        """
        if id == None: 
            self.id = uuid.uuid4().int  # unique id
        else:
            self.id = id
        self.condition = condition # assign condition value

    def get_category(self):
        """
        Returns the name of the class as a string.

        Written By Mariya Mokrynska
        """
        return self.__class__.__name__

# WAVE 3

    # Returns a string representation of the Item instance
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
# WAVE 5

    def condition_description(self):
        if self.condition == 0:
            return "poor"
        elif self.condition == 1:
            return "not so bad"
        elif self.condition == 2:
            return "fair"
        elif self.condition == 3:
            return "still has a life in it"
        elif self.condition == 4:
            return "like new"
        elif self.condition == 5:
            return "new with tag"
        else:
            return "Unknown condition"
