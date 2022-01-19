import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data and 
        
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there is no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None
        * If there is no start or user provided end node in the graph, inform the user

        """
        assert self.graph.has_node(start), 'start node is not in the graph.'

        if end:
            assert self.graph.has_node(end), 'end node is not in the graph.'

        if start == end:
            print('Start and end node are the same.')
            return

        bfs_dict = {
            'queue':[[start]],
            'traversal':[],
            'paths':[]}

        while bfs_dict['queue']:
            current_path = bfs_dict['queue'].pop(0)
            current_vertex = current_path[-1]
            if current_vertex not in bfs_dict['traversal']:
                bfs_dict['traversal'].append(current_vertex)
                for neighbor in self.graph.neighbors(current_vertex):
                    path_traversal = list(current_path)
                    path_traversal.append(neighbor)
                    bfs_dict['queue'].append(path_traversal)
                    bfs_dict['paths'].append(path_traversal)
        
        assert all(node in self.graph.nodes for node in bfs_dict['traversal']) == True

        if end:
            path_list = [path for path in bfs_dict['paths'] if path[0]==start and path[-1] == end]
            if len(path_list) == 0:
                print('A path does not exist for start ' + start + ' and end ' + end + ' nodes.')
                return
            if len(path_list) > 1:
                path_length_list = [len(path) for path in path_list]
                shortest_path_length = min(path_length_list)
                shortest_path_list = [path_list[i] for i,x in enumerate(path_length_list) if x == shortest_path_length]
                if len(shortest_path_list) > 1:
                    print('There are ' + str(len(shortest_path_list)) + ' shortest paths of length ' + str(shortest_path_list) + \
                         '. Returning all possible shortest paths.')
                    return shortest_path_list
                else:
                    return shortest_path_list[0]
            else:
                return path_list[0]
        else:
            return bfs_dict['traversal']