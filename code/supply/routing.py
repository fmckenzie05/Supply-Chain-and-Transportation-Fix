import networkx as nx

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
path = nx.shortest_path(G, "Factory", "Retailer")

# Print the path to the user
print("The shortest path from the factory to the retailer is:")
print(path)