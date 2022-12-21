class Shipment:
    def __init__(self, tracking_number, sender, recipient, status):
        self.tracking_number = tracking_number
        self.sender = sender
        self.recipient = recipient
        self.status = status
        self.history = [status]
    
    def update_status(self, new_status):
        self.status = new_status
        self.history.append(new_status)
    
    def __str__(self):
        return f"Tracking Number: {self.tracking_number}\nSender: {self.sender}\nRecipient: {self.recipient}\nStatus: {self.status}"

class ShipmentTracker:
    def __init__(self):
        self.shipments = {}
    
    def add_shipment(self, shipment):
        self.shipments[shipment.tracking_number] = shipment
    
    def update_status(self, tracking_number, new_status):
        shipment = self.shipments.get(tracking_number)
        if shipment:
            shipment.update_status(new_status)
    
    def get_status(self, tracking_number):
        shipment = self.shipments.get(tracking_number)
        if shipment:
            return shipment.status
    
    def get_history(self, tracking_number):
        shipment = self.shipments.get(tracking_number)
        if shipment:
            return shipment.history
    
    def __str__(self):
        return "\n".join([str(shipment) for shipment in self.shipments.values()])

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
