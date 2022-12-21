"""Repository for all the functions in the supply chain"""

# import networkx as nx # What is this?

# Define a dictionary to store the inventory
inventory = {
    "apples": 100,
    "oranges": 50,
    "bananas": 75
}

# Define a function to display the inventory
def display_inventory():
    """Displays the inventory"""
    print("Current inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

# Define a function to restock the inventory
def restock_inventory(item, quantity):
    """Restocks the inventory"""
    if item in inventory:
        inventory[item] += quantity
        print(f"{quantity} {item} added to the inventory.")
    else:
        inventory[item] = quantity
        print(f"{item} added to the inventory with a quantity of {quantity}.")

# Define a function to sell items from the inventory
def sell_item(item, quantity):
    """Sells the item and removes it from inventory"""
    if item in inventory and inventory[item] >= quantity:
        inventory[item] -= quantity
        print(f"{quantity} {item} sold.")
    elif item not in inventory:
        print(f"{item} is not in the inventory.")
    else:
        print(f"There are only {inventory[item]} {item} in the inventory.")

class Order:
    """Class for ordering inventory from the Warehouse"""
    def __init__(self, order_id, product, quantity, price):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.price = price
        self.total_cost = self.quantity * self.price

    def __str__(self):
        return f"Order ID: {self.order_id}\nProduct: {self.product}\nQuantity: {self.quantity}\nPrice: {self.price:.2f}\nTotal Cost: {self.total_cost:.2f}"

class OrderManager:
    """Manages the ordering"""
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        """function that adds orders"""
        self.orders.append(order)

    def remove_order(self, order_id):
        """Removes orders"""
        for order in self.orders:
            if order.order_id == order_id:
                self.orders.remove(order)
                break

    def get_total_cost(self):
        """Gets the total cost"""
        total_cost = 0
        for order in self.orders:
            total_cost += order.total_cost
        return total_cost

    def print_orders(self):
        """Prints the order"""
        for order in self.orders:
            print(order)


class Shipment:
    """creates shipments"""
    def __init__(self, tracking_number, sender, recipient, status):
        self.tracking_number = tracking_number
        self.sender = sender
        self.recipient = recipient
        self.status = status
        self.history = [status]

    def update_status(self, new_status):
        """updates the shipment status"""
        self.status = new_status
        self.history.append(new_status)

    def __str__(self):
        return f"""'Tracking Number: {self.tracking_number}\n'
                   'Sender:          {self.sender}\n'
                   'Recipient:       {self.recipient}\n'
                   'Status:          {self.status}'"""

class ShipmentTracker:
    """Defines the  Shipment tracking class"""
    def __init__(self):
        self.shipments = {}

    def __str__(self):
        return "\n".join([str(shipment) for shipment in self.shipments.values()])

    def add_shipment(self, shipment):
        """Adds a shipment to the db"""
        self.shipments[shipment.tracking_number] = shipment

    def update_status(self, tracking_number, new_status):
        """Updates the db tracking number"""
        shipment = self.shipments.get(tracking_number)
        return shipment.update_status(new_status)


    def get_status(self, tracking_number):
        """Tracks the status of the Shipment"""
        shipment = self.shipments.get(tracking_number)
        return shipment.status

    def get_history(self, tracking_number):
        """Gets the history of the shipment"""
        shipment = self.shipments.get(tracking_number)
        return shipment.history


class Warehouse:
    """Defines the Warehouse class"""
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
        for i in self.items:
            if i.name == item_name:
                return i
        return None

    def get_item_count(self):
        """Returns the number of items in the warehouse."""
        return len(self.items)


class ImpEx(Warehouse):
    """Warehouse Class for import / export"""

    def receive_shipment(self, items):
        """Receives a shipment and adds the items to the warehouse."""
        self.items += items

    def ship_item(self, item):
        """Ships an item from the warehouse."""
        self.items.remove(item)

    def get_inventory(self):
        """Returns a list of items in the warehouse."""
        return self.items


class Warehouse:
    """Warehouse Shipping and Receiving Operations"""
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
        """Searches for an item by name and returns
        the item if found, or None if not found."""
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def get_item_count(self):
        """Returns the number of items in the warehouse."""
        return len(self.items)

    def get_inventory(self):
        """Returns a list of tuples containing the
        name and quantity of each item in the warehouse."""
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
    """Defines items"""
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


# Test the functions
display_inventory()
restock_inventory("apples", 50)
display_inventory()
sell_item("apples", 75)
display_inventory()

# Test the OrderManager
manager = OrderManager()

# Add some orders
manager.add_order(Order(1, "Apple", 10, 0.5))
manager.add_order(Order(2, "Orange", 5, 0.75))
manager.add_order(Order(3, "Banana", 20, 0.25))

# Print the orders
print("All orders:")
manager.print_orders()

# Remove an order
manager.remove_order(2)

# Print the updated list of orders
print("\nUpdated orders:")
manager.print_orders()

# Print the total cost of the orders
print(f"\nTotal cost: {manager.get_total_cost():.2f}")

# Test the Warehouse class
WaH = Warehouse

# Add some items to the warehouse
WaH.receive_shipment(['table', 'chair', 'desk'])

# Print the current inventory
print(WaH.get_inventory())

# Ship an item
WaH.ship_item('chair')

# Print the updated inventory
print(WaH.get_inventory())


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

# Test the Warehouse and Item classes
warehouse = Warehouse('Warehouse 1', 'New York')


# Print the inventory
print(warehouse.get_inventory())

# Restock an item
warehouse.restock('Widget 1', 50)

# Print the updated inventory
print(warehouse.get_inventory())


# Test the ShipmentTracker
tracker = ShipmentTracker()

# Add some shipments
tracker.add_shipment(Shipment("123456", "Alice", "Bob", "In transit"))
tracker.add_shipment(Shipment("789012", "Charlie", "Dave", "Delivered"))

# Print the shipments
print("All shipments:")
print(tracker)

# Update the status of a shipment
tracker.update_status("123456", "Delivered")

# Print the updated shipment
print("\nUpdated shipment:")
print(tracker.get_status("123456"))

# Print the history of a shipment
print("\nHistory of shipment 123456:")
print(tracker.get_history("123456"))

"""
# Create an empty graph
G = nx.Graph()

# Add nodes representing the different locations in the supply chain
G.add_node("Factory")
G.add_node("Warehouse 1")
G.add_node("Warehouse 2")
G.add_node("Retailer")

# Add edges representing the flow of goods between locations
G.add_edge("Factory", "Warehouse 1")
G.add_edge("Factory", "Warehouse 2")
G.add_edge("Warehouse 1", "Retailer")
G.add_edge("Warehouse 2", "Retailer")

# Use NetworkX to find the shortest path between the factory and the retailer
# Then Print the path to the user
path = nx.shortest_path(G, "Factory", "Retailer")
print(f"The shortest path from the factory to the retailer is:\n{path}")
"""
