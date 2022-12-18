# Warehouse Shipping and Receiving Operations

class Warehouse:
    def __init__(self):
        self.items = []

    def receive_shipment(self, items):
        """Receives a shipment and adds the items to the warehouse."""
        self.items += items

    def ship_item(self, item):
        """Ships an item from the warehouse."""
        self.items.remove(item)

    def get_inventory(self):
        """Returns a list of items in the warehouse."""
        return self.items

# Test the Warehouse class
warehouse = Warehouse()

# Add some items to the warehouse
warehouse.receive_shipment(['table', 'chair', 'desk'])

# Print the current inventory
print(warehouse.get_inventory())

# Ship an item
warehouse.ship_item('chair')

# Print the updated inventory
print(warehouse.get_inventory())
