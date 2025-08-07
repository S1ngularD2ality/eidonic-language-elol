import networkx as nx

def pathweaver(graph, start, end):
    """
    graph: networkx graph with obstacles as weights
    start, end: node labels
    """
    path = nx.shortest_path(graph, start, end, weight='weight')
    return path
