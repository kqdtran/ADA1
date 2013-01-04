# Algorithms: Design and Analysis Part 1, Coursera
# Week 5 Problem: Dijkstra's Shortest Path Algorithm in Directed Graph
# Much of the source code adapted from http://code.activestate.com/recipes/119466-dijkstras-algorithm-for-shortest-paths/
# Many thanks to David Eppstein, UC Irvine for the excellent source code and description

import sys
from priodict import priority_dict

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

    # populate the graph using data from the text file via dictionary comprehensions
    G = {int(line.split()[0]): {(int(tup.split(',')[0])): int(tup.split(',')[1])
                                for tup in line.split()[1:] if tup} for line in line_list if line}
    f.close()
    return G

def dijkstra(G, start, end=None):
    """Find shortest paths from the start vertex to all
    vertices nearer than or equal to the end.

    The input graph G is assumed to have the following
    representation: A vertex can be any object that can
    be used as an index into a dictionary.  G is a
    dictionary, indexed by vertices.  For any vertex v,
    G[v] is itself a dictionary, indexed by the neighbors
    of v.  For any edge v->w, G[v][w] is the length of
    the edge.  This is related to the representation in
    <http://www.python.org/doc/essays/graphs.html>
    where Guido van Rossum suggests representing graphs
    as dictionaries mapping vertices to lists of neighbors,
    however dictionaries of edges have many advantages
    over lists: they can store extra information (here,
    the lengths), they support fast existence tests,
    and they allow easy modification of the graph by edge
    insertion and removal.  Such modifications are not
    needed here but are important in other graph algorithms.
    Since dictionaries obey iterator protocol, a graph
    represented as described here could be handed without
    modification to an algorithm using Guido's representation.

    Of course, G and G[v] need not be Python dict objects;
    they can be any other object that obeys dict protocol,
    for instance a wrapper in which vertices are URLs
    and a call to G[v] loads the web page and finds its links.
    
    The output is a pair (D,P) where D[v] is the distance
    from start to v and P[v] is the predecessor of v along
    the shortest path from s to v.
    
    Dijkstra's algorithm is only guaranteed to work correctly
    when all edge lengths are positive. This code does not
    verify this property for all edges (only the edges seen
    before the end vertex is reached), but will correctly
    compute shortest paths even for some graphs with negative
    edges, and will raise an exception if it discovers that
    a negative edge has caused it to make a mistake.

    Input: G - the input graph in the adjacency list representation via a dictionary
    start - the starting vertex
    end - the ending vertex. It is not necessary to provide this argument, in that case dijkstra's will find the distance
    from 'start' to every other vertex, but that may take a long time, so it is recommended to provide the last argument"""

    D = {}	          # dictionary of final distances
    P = {}	          # dictionary of predecessors
    Q = priority_dict()   # est.dist. of non-final vert.
    
    # initialize Q and P
    for vertex in G:
        Q[vertex] = float("inf")
        P[vertex] = None
    
    Q[start] = 0
    
    for v in Q: # iterate and pop the smallest item in Q
        D[v] = Q[v]
        if v == end: break # we have reached the end

        for w in G[v]: # for all of v's adjacent vertices
            vwLength = D[v] + G[v][w]
            if w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v

    return D, P

def findshortestPath(G, start, end):
    """Find a single shortest path from the given start vertex to the given end vertex.
    The input has the same conventions as dijkstra().
    The output is a list of the vertices in order along
    the shortest path.

    Input: G - the input graph in the adjacency list representation via a dictionary
    start - the starting vertex
    end - the ending vertex

    Note: This method is not needed in the current exercise, however, it would be nice to know the shortest path from one vertex to another sometimes"""

    _, P = dijkstra(G, start, end)
    path = []
    while 1:
        path.append(end)
        if end == start: break
        end = P[end] # find the next predecessor
    path.reverse() # reverse the list since we are appending from the back
    return path
    
def main():
    G = make_graph('dijkstraData.txt')
    lst = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197] # a list of all the desired ending vertices
    for v in lst:
        D, _ = dijkstra(G, 1, v)
        if v != lst[-1]:
            print(D[v], end=",")
        else:
            print(D[v])
    
if __name__ == '__main__':
    main()
