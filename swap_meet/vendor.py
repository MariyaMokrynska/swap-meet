# WAVE 1

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, item_to_remove):
        if item_to_remove not in self.inventory:
            return False
        self.inventory.remove(item_to_remove)
        return item_to_remove


# WAVE 2

    def get_by_id(self, id):
        """
        Searches for an item in the inventory by its ID.
        Returns the item if found, otherwise returns None.

        Written By Mariya Mokrynska
        """
        for item in self.inventory:
            if item.id == id:
                return item
        return None

# WAVE 3

    def swap_items(self, other_vendor, my_item, their_item):
        # Swap fails if item is missing in self or other_vendor inventory
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        # Successful swap: remove and add the items from/to self and other_vendor inventories
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)

        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)

        return True


# WAVE 4
# version 1
#    def swap_first_item(self, other_vendor):
        """ 
        Swap the first item in each vendor's inventory if both have items.

        Args:
            other_vendor (Vendor): The vendor to swap with.

        Returns:
            bool: True if the swap is successful, False otherwise.

        Written By Mariya Mokrynska
        """
#        if self.inventory != [] and other_vendor.inventory != []:
#            my_item_to_remove = self.remove(self.inventory[0])
#            other_vendor.add(my_item_to_remove)

#            other_vendor_item_to_remove = other_vendor.remove(
#                other_vendor.inventory[0])
#            self.add(other_vendor_item_to_remove)
#            return True
#        return False


# WAVE 4
# version 2

    def swap_first_item(self, other_vendor):
        """
        Swap the first item in the inventory with another vendor's first item.

        If either inventory is empty, the swap does not happen and returns False. 
        Otherwise, it swaps the first item from each vendor's inventory.

        Written By Mariya Mokrynska
        """
        # if self.inventory == [] or other_vendor.inventory == []:
        #    return False
        if not self.inventory or not other_vendor.inventory:
            return False

        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_item, their_item)

# WAVE 6

    def get_by_category(self, category):
        """
        Get all items in the inventory that match the given category.
        """
        return [item for item in self.inventory if item.get_category() == category]

    def get_best_by_category(self, category):
        """
        Get the item with the highest condition in the given category.
        """
        # best_item = None
        # highest_condition = -1

        # for item in self.inventory:
        #     if item.get_category() == category:
        #         if item.condition > highest_condition:
        #             highest_condition = item.condition
        #             best_item = item

        # return best_item
        
        # Refactored version

        items_in_category = self.get_by_category(category)
        if not items_in_category:
            return None
        
        return max(items_in_category, key=lambda item: item.condition)

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        """
        Swap the best item of a given category with another vendor's best item 
        from a different category.

        Written By Mariya Mokrynska
        """
        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)

        # Ensure both items exist before swapping
        if not my_item or not their_item:
            return False

        return self.swap_items(other_vendor, my_item, their_item)
