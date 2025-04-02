from .item import Item

# WAVE 1


class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, item_to_remove):
        if item_to_remove in self.inventory:
            self.inventory.remove(item_to_remove)
            return item_to_remove
        return False

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
    def swap_first_item(self, other_vendor):
        """
        Swap the first item in each vendor's inventory if both have items.

        Args:
            other_vendor (Vendor): The vendor to swap with.

        Returns:
            bool: True if the swap is successful, False otherwise.

        Written By Mariya Mokrynska
        """
        if self.inventory != [] and other_vendor.inventory != []:
            my_item_to_remove = self.remove(self.inventory[0])
            other_vendor.add(my_item_to_remove)

            other_vendor_item_to_remove = other_vendor.remove(
                other_vendor.inventory[0])
            self.add(other_vendor_item_to_remove)
            return True
        return False
