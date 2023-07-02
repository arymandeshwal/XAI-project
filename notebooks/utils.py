import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import os

def create_nx_graph(data):
    # extracting the node and edge information to create a networkx graph so that we can calculate degree distribution
    edge_index = data['user',"rates",'movie']["edge_index"]
    user = [ f"U{int(i)}" for i in edge_index[0].unique()]
    movie = [ f"M{int(i)}" for i in edge_index[1].unique()]
    edges = [(f"U{int(edge_index[0][i])}",f"M{int(edge_index[1][i])}") for i in range(len(edge_index[0]))]

    # creating a heterogenous networkx graph

    hetero_graph = {'movie': movie,'user': user}
    edges_graph = {'user-rates-movie': edges}

    # Creating a NetworkX graph object
    graph = nx.Graph()

    # Adding nodes to the graph with node type information
    for node_type in hetero_graph:
        nodes = hetero_graph[node_type]
        for node in nodes:
            graph.add_node(node, type=node_type)

    # Adding edges to the graph
    for edge_type in edges_graph:
        edges = edges_graph[edge_type]
        if isinstance(edges[0], tuple):
            # If the edges are tuples, add them directly
            graph.add_edges_from(edges, label=edge_type)
            
    return graph

def save_target_nodes(user, movie):
    with open('target.txt','a') as f:
        target = str(movie) + "," + str(user)+"\n"
        f.write(target)

def retrieve_target_nodes():
    file_name = 'target.txt'
    with open(file_name,'r') as f:
        target = f.readline().split(',')
        movie, user = int(target[0]), int(target[1])
    
    os.remove(file_name)
    return movie, user


def target_graph_plot(index,data,train_data):
    target_edge_index = int(index)

    t_user = int(train_data["user", "rates", "movie"].edge_label_index[0][target_edge_index])
    t_movie = int(train_data["user", "rates", "movie"].edge_label_index[1][target_edge_index])
    print(f"User:{t_user} ----rates----> {t_movie}")

    save_target_nodes(t_user,t_movie)

    print("Graph being created")
    graph = create_nx_graph(data)
    print("Graph created")

    graph.add_node(t_user,type = "Target_user")
    graph.add_node(t_movie,type = "Target_movie")
    graph.add_edge(t_user,t_movie, label='Target_edge')
    # Specify node colors based on node types
    node_colors = {
        'movie': (0.69, 0.88, 0.9),
        'user': (0.56, 0.93, 0.56),
        'Target_user': (1.0, 0.0, 0.0),
        'Target_movie': (0.98, 0.502, 0.447)
    }

    # Specify edge colors based on edge types
    edge_colors = {
        'user-rates-movie': (0.8, 0.8, 0.8),
        'Target_edge': (0, 0,0)
    }

    # Create a layout for the graph
    layout = nx.spring_layout(graph, k = 1)
    plt.figure(figsize=(10, 8))
    # Draw nodes and edges
    node_color = [node_colors[graph.nodes[node]['type']] for node in graph.nodes()]
    edge_color = [edge_colors[graph.edges[edge]['label']] for edge in graph.edges()]
    nx.draw(graph, pos=layout, node_color=node_color, edge_color=edge_color, with_labels=True, node_size = 500)

    legend_labels = list(node_colors.keys()) + list(edge_colors.keys())
    legend_colors = list(node_colors.values())+ list(edge_colors.values())
    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in legend_colors]
    plt.legend(legend_elements, legend_labels)
    plt.show()


def graph2df ( gdata, data, link_exists, file_name, index ):

    tabular = []
    for i in range(len(gdata[0])):
        row = []
        movie_index = int(gdata[index][i])
        
        row.append(movie_index)        
        row.extend([int(j) for j in data['movie'].x[movie_index]])
        row.append(int(gdata[0][i]))
        row.append(link_exists)
        tabular.append(row)

    df = pd.DataFrame(tabular, columns=["movie_id",'(no genres listed)', 'Action', 'Adventure', 'Animation', 'Children',
        'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir',
        'Horror', 'IMAX', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller',
        'War', 'Western',"user_id","link_exists"])
    df.to_csv(file_name,index=False)
