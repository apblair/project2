# write tests for bfs
import pytest
import networkx as nx
from search import *

# @pytest.fixture
def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    adj_file = './data/tiny_network.adjlist'
    start_node  = 'Nevan Krogan'

    bfs_traversal = Graph(adj_file).bfs(start_node)
    nx_graph = nx.read_adjlist(adj_file, create_using=nx.DiGraph, delimiter=";")

    assert all(node in nx_graph.nodes for node in bfs_traversal) == True
    nx_bfs_traversal_nodes = list(nx.bfs_tree(nx_graph, start_node).nodes)
    assert all([True for node in range(len(bfs_traversal)) if bfs_traversal[node] == nx_bfs_traversal_nodes[node]]) == True

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    bfs_traversal = Graph('./data/.citation_network.adjlist').bfs('Nevan Krogan')

test_bfs_traversal()
# print(nx.shortest_path(self.graph, source=start, target=end))


