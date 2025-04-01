class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, item_to_remove):
        self.inventory.remove(item_to_remove)
        if not item_to_remove in self.inventory:
            return False
        return item_to_remove
