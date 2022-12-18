# Finance Operations

class Finance:
    def __init__(self):
        self.expenses = []
        self.revenue = []

    def add_expense(self, amount, description):
        """Adds an expense to the finance department."""
        self.expenses.append((amount, description))

    def add_revenue(self, amount, description):
        """Adds revenue to the finance department."""
        self.revenue.append((amount, description))

    def get_balance(self):
        """Calculates and returns the balance (revenue - expenses) of the finance department."""
        total_expenses = sum(expense[0] for expense in self.expenses)
        total_revenue = sum(revenue[0] for revenue in self.revenue)
        return total_revenue - total_expenses

# Test the Finance class
finance = Finance()

# Add some expenses and revenue
finance.add_expense(100, 'supplies')
finance.add_expense(200, 'rent')
finance.add_revenue(500, 'sales')
finance.add_revenue(300, 'consulting')

# Print the balance
print(finance.get_balance())
