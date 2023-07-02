import networkx as nx
from utils import create_nx_graph

def graph_analysis (data):
#data = torch.load("notebook/graph.pt")
    graph = create_nx_graph(data)

    # Printing node and edge information
    print(f"Total number of nodes: {graph.number_of_nodes()}")
    print(f"Total number of edges: {graph.number_of_edges()}")

    # Calculating degree distribution
    degree_sequence = [degree for _, degree in graph.degree()]
    # Calculating average node degree
    average_degree = sum(degree_sequence) / len(degree_sequence)

    print(f"Average Node Degree: {average_degree}")
