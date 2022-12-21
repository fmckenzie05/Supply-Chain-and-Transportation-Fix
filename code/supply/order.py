class Order:
    def __init__(self, order_id, product, quantity, price):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.price = price
        self.total_cost = self.quantity * self.price

    def __str__(self):
        return f"Order ID: {self.order_id}\nProduct: {self.product}\nQuantity: {self.quantity}\nPrice: {self.price:.2f}\nTotal Cost: {self.total_cost:.2f}"

class OrderManager:
    def __init__(self):
        self.orders = []
    
    def add_order(self, order):
        self.orders.append(order)
    
    def remove_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                self.orders.remove(order)
                break
    
    def get_total_cost(self):
        total_cost = 0
        for order in self.orders:
            total_cost += order.total_cost
        return total_cost
    
    def print_orders(self):
        for order in self.orders:
            print(order)

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