# Define a dictionary to store the inventory
inventory = {
    "apples": 100,
    "oranges": 50,
    "bananas": 75
}

# Define a function to display the inventory
def display_inventory():
    print("Current inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

# Define a function to restock the inventory
def restock_inventory(item, quantity):
    if item in inventory:
        inventory[item] += quantity
        print(f"{quantity} {item} added to the inventory.")
    else:
        inventory[item] = quantity
        print(f"{item} added to the inventory with a quantity of {quantity}.")

# Define a function to sell items from the inventory
def sell_item(item, quantity):
    if item in inventory and inventory[item] >= quantity:
        inventory[item] -= quantity
        print(f"{quantity} {item} sold.")
    elif item not in inventory:
        print(f"{item} is not in the inventory.")
    else:
        print(f"There are only {inventory[item]} {item} in the inventory.")

# Test the functions
display_inventory()
restock_inventory("apples", 50)
display_inventory()
sell_item("apples", 75)
display_inventory()