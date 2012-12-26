# Algorithms: Design and Analysis Part 1, Coursera
# Week 4 Material: Topological Sort using Depth First Search

def dfs(G, s, explored, distance, current_label):
    """Performs a depth first search in graph G starting from vertex s
    Input: G - the input graph in the adjacency list representation via a dictionary
    s - the starting vertex
    explored - a set of explored vertices
    distance - a dictionary representing the topological order of the vertices
    current_label - the current order of the topological order, disguised as a mutable list"""
    
    explored.add(s)
    for v in G[s]: # for every edge (s, v)
        if v not in explored:
            dfs(G, v, explored, distance, current_label)
    distance[current_label[0]] = s
    current_label[0] -= 1

def topological_sort(G, distance):
    """Performs and outputs a topological sort of graph G using dfs
    Input: G - the input graph in the adjacency list representation via a dictionary
    distance - a dictionary representing the topological order of the vertices"""

    explored = set()
    current_label = [len(G)]
    for v in G.keys():
        if v not in explored:
            dfs(G, v, explored, distance, current_label)
    
def main():
    f = open('topo.txt', 'r')
    line_list = f.readlines()
    G = {str(line.split()[0]): [str(val) for val in line.split()[1:] if val] for line in line_list if line}
    print("G:", G)
    distance = dict()
    topological_sort(G, distance)
    topo = iter(sorted(distance.items()))
    print("A topological order of G is:", end=" ")
    for _, vertex in topo:
        print(vertex, end=" ")
    print()

if __name__ == '__main__':
    main()
