# Sales Operations

class Sales:
    def __init__(self):
        self.sales = []

    def record_sale(self, amount, customer):
        """Records a sale."""
        self.sales.append((amount, customer))

    def get_sales(self):
        """Returns a list of recorded sales."""
        return self.sales

    def get_total_sales(self):
        """Calculates and returns the total amount of recorded sales."""
        return sum(sale[0] for sale in self.sales)

# Test the Sales class
sales = Sales()

# Record some sales
sales.record_sale(100, 'Alice')
sales.record_sale(200, 'Bob')
sales.record_sale(300, 'Charlie')

# Print the recorded sales
print(sales.get_sales())

# Print the total sales
print(sales.get_total_sales())
