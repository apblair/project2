# write tests for bfs
import pytest
import networkx as nx
from search import *

@pytest.fixture
def test_bfs_traversal():
    """
    Unit test for checking if all nodes were traversed and in BFS order.

    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    adj_file = './data/tiny_network.adjlist'
    start  = 'Nevan Krogan'

    bfs_traversal = Graph(adj_file).bfs(start)
    nx_graph = nx.read_adjlist(adj_file, create_using=nx.DiGraph, delimiter=";")

    # Check if all nodes were traversed
    assert all(node in nx_graph.nodes for node in bfs_traversal) == True

    # Check if nodes are traversed in the right order using networkx's bfs_tree method.
    nx_bfs_traversal_nodes = list(nx.bfs_tree(nx_graph, start).nodes)
    assert all([True for node in range(len(bfs_traversal)) if bfs_traversal[node] == nx_bfs_traversal_nodes[node]]) == True

def test_bfs():
    """
    Unit test for checking connected or unconnected nodes and shortest path(s).

    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    adj_file = './data/citation_network.adjlist'
    nx_graph = nx.read_adjlist(adj_file, create_using=nx.DiGraph, delimiter=";")
    print(type(nx_graph))

    # Check if nodes are connected, and return the shortest path using network's shortest_path method.
    start = 'Nadav Ahituv'
    end = 'Ryan Corces'
    shortest_path = Graph(adj_file).bfs(start, end)
    assert shortest_path == nx.shortest_path(nx_graph, start, end)

    # Check if non-connected nodes return None
    start = 'Jimmie Ye'
    end = 'Atul Butte'
    shortest_path = Graph(adj_file).bfs(start, end)
    assert shortest_path == None

    # Check if multiple shortest paths are returned, and in network's shortest_path method.
    start = 'Vasilis Ntranos'
    end = 'Yin Shen'
    shortest_path = Graph(adj_file).bfs(start, end)
    assert len(shortest_path) > 1
    assert nx.shortest_path(nx_graph, start, end) in shortest_path