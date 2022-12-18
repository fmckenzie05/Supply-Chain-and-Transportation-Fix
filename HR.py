# HR Operations

class HR:
    def __init__(self):
        self.employees = []

    def hire(self, employee):
        """Hires an employee."""
        self.employees.append(employee)

    def fire(self, employee):
        """Fires an employee."""
        self.employees.remove(employee)

    def get_employee_names(self):
        """Returns a list of employee names."""
        return [employee.name for employee in self.employees]

class Employee:
    def __init__(self, name):
        self.name = name

# Test the HR and Employee classes
hr = HR()

# Hire some employees
hr.hire(Employee('Alice'))
hr.hire(Employee('Bob'))
hr.hire(Employee('Charlie'))

# Print the list of employee names
print(hr.get_employee_names())

# Fire an employee
hr.fire(Employee('Bob'))

# Print the updated list of employee names
print(hr.get_employee_names())
