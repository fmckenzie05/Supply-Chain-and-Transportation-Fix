# IT Department Framework for Warehouse Network and Security Operations

class ITDepartment:
    def __init__(self, name):
        self.name = name
        self.network_devices = []
        self.security_policies = []

    def add_network_device(self, device):
        """Adds a network device to the warehouse."""
        self.network_devices.append(device)

    def remove_network_device(self, device):
        """Removes a network device from the warehouse."""
        self.network_devices.remove(device)

    def get_network_devices(self):
        """Returns a list of network devices in the warehouse."""
        return self.network_devices

    def add_security_policy(self, policy):
        """Adds a security policy to the warehouse."""
        self.security_policies.append(policy)

    def remove_security_policy(self, policy):
        """Removes a security policy from the warehouse."""
        self.security_policies.remove(policy)

    def get_security_policies(self):
        """Returns a list of security policies in the warehouse."""
        return self.security_policies

# Test the ITDepartment class
it_department = ITDepartment('Warehouse IT')

# Add some network devices to the warehouse
it_department.add_network_device('router')
it_department.add_network_device('switch')
it_department.add_network_device('firewall')

# Print the list of network devices
print(it_department.get_network_devices())

# Remove a network device
it_department.remove_network_device('switch')

# Print the updated list of network devices
print(it_department.get_network_devices())

# Add some security policies to the warehouse
it_department.add_security_policy('password policy')
it_department.add_security_policy('access control policy')

# Print the list of security policies
print(it_department.get_security_policies())

# Remove a security policy
it_department.remove_security_policy('access control policy')

# Print the updated list of security policies
print(it_department.get_security_policies())

