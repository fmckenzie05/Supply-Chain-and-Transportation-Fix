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

# Print the number of items in the warehouse
print(warehouse.get_item_count())

# Search for an item by name
item = warehouse.search_item('Widget 2')
print(item.name)
print(item.quantity)
print(item.price)

# Remove an item
warehouse.remove_item(item)

# Print the updated number of items in the warehouse
print(warehouse.get_item_count())
