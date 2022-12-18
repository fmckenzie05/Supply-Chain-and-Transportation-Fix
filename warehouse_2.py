class Warehouse:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []

    def add_item(self, item):
        """Adds an item to the warehouse."""
        self.items.append(item)

    def remove_item(self, item):
        """Removes an item from the warehouse."""
        self.items.remove(item)

    def search_item(self, item_name):
        """Searches for an item by name and returns the item if found, or None if not found."""
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def get_item_count(self):
        """Returns the number of items in the warehouse."""
        return len(self.items)

    def get_inventory(self):
        """Returns a list of tuples containing the name and quantity of each item in the warehouse."""
        inventory = []
        for item in self.items:
            inventory.append((item.name, item.quantity))
        return inventory

    def restock(self, item_name, quantity):
        """Adds the specified quantity of the specified item to the warehouse."""
        item = self.search_item(item_name)
        if item:
            item.quantity += quantity
        else:
            self.add_item(Item(item_name, quantity, 0))

    def process_order(self, item_name, quantity):
        """Removes the specified quantity of the specified item from the warehouse."""
        item = self.search_item(item_name)
        if item and item.quantity >= quantity:
            item.quantity -= quantity
        else:
            print(f'Error: Insufficient quantity of {item_name} in warehouse.')

class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

# Test the Warehouse and Item classes
warehouse = Warehouse('Warehouse 1', 'New York')

# Add some items to the warehouse
warehouse.add_item(Item('Widget 1', 100, 10.99))
warehouse.add_item(Item('Widget 2', 200, 12.99))
warehouse.add_item(Item('Widget 3', 300, 14.99))

# Print the inventory
print(warehouse.get_inventory())

# Restock an item
warehouse.restock('Widget 1', 50)

# Print the updated inventory
print(warehouse.get_inventory())
