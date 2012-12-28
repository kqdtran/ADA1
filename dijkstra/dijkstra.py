# Algorithms: Design and Analysis Part 1, Coursera
# Week 5 Problem: Dijkstra's Algorithm

def make_graph(filename):
    """Make a graph from the data stored inside the text file
    The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200.
    Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge.
    Input: filename - the name of the text file"""

    try: 
        f = open(filename, 'r')
    except IOError:
        sys.exit("No such file!")
        
    line_list = f.readlines()
    n = int(line_list[len(line_list)-1].split()[0]) # largest vertex number
    G = {i: [] for i in range(1, n+1)} # construct an empty list of adjacent nodes for every vertex
    GT = {i: [] for i in range(1, n+1)} # G's Transpose

    # Read in the data from the text file and add them to the graphs
    for line in line_list:
        curr_line = line.split()
        v1 = int(curr_line[0])
        v2 = int(curr_line[1])
        G[v1].append(v2)
        GT[v2].append(v1)
    f.close()
    return G, GT
