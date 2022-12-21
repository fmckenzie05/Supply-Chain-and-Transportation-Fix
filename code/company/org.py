"""Simple Organizational Design Structure"""

class Organization:
    """Organization class for implementing the organizations functions"""
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.employees = []

    def add_employee(self, employee):
        """Adds an employee to the organization."""
        self.employees.append(employee)

    def remove_employee(self, employee):
        """Removes an employee from the organization."""
        self.employees.remove(employee)

    def get_employees(self):
        """Returns a list of employees in the organization."""
        return self.employees

class Employee:
    """Employee class"""
    def __init__(self, name):
        self.name = name

    def work(self):
        """Simulates an employee working."""
        print(f'{self.name} working')

# Test the Organization and Employee classes
organization = Organization('Acme Inc.', 'John Smith')

# Add some employees to the organization
organization.add_employee(Employee('Alice'))
organization.add_employee(Employee('Bob'))
organization.add_employee(Employee('Charlie'))

# Print the list of employees
print(organization.get_employees())

# Remove an employee
organization.remove_employee(Employee('Bob'))

# Print the updated list of employees
print(organization.get_employees())
