# Algorithms: Design and Analysis Part 1, Coursera
# Problem 3: Find the minimum cut in a graph represented by the adjacency list using Karger's algorithm

from random import choice
from copy import deepcopy

def contract(vert1, vert2, G):
    """Contracts two vertices from a randomly chosen edge in graph G into one single vertex
    vert1 = the first vertex
    vert2 = the second vertex, which will be shrinked into vert1
    G = the input graph, represented by a dictionary"""
    
    G[vert1].extend(G[vert2]) # append vert2's list to vert1's list
    for adj_vert in G[vert2]: # for every adjacent node of vert2
        lst = G[adj_vert]
        for i in range(0, len(lst)): # scan its list and replace vert2 with vert1
            if lst[i] == vert2:
                lst[i] = vert1
            
    while vert1 in G[vert1]: # remove self-loop in vert1's list
        G[vert1].remove(vert1)    
    del G[vert2] # remove vert2 and its list from the graph

def findMinCut(G):
    """Find the minimum cut in the graph G using Karger's algorithm
    Note: In what I used to find a random edge below, the probability of an edge is chosen is not
    really uniformly distributed, but I think it's good enough for the purpose of this problem.
    G = the input graph, represented by a dictionary"""
    
    while len(G) > 2: # while there are more than two vertices in G
        vert1 = choice(list(G.keys())) # choose a first random vertex
        vert2 = choice(G[vert1]) # choose a second random vertex from 1st's list, i.e. choose a random edge from G
        contract(vert1, vert2, G) # contract vert2 into vert1
    return len(G.popitem()[1]) # pop one of the two remaining elements, return the size of its list, which is also the min cut

def main():
    """Find the minimum cut in the graph G using Karger's algorithm after n*n*logn repeated trials.
    The probability of failing to find a min cut after n*n*logn trials can be shown to be 1/n
    In the code below, I actually ran it 1000 times only... because waiting for 200*200*log(200) iterations can be very long."""
    
    f = open('kargerMinCut.txt', 'r')
    line_list = f.readlines()
    G = {int(line.split()[0]): [int(val) for val in line.split()[1:] if val] for line in line_list if line}
    mincut = float("inf") # set mincut to positive infinity

    # loop 1000 times and calculate the min cut. It may take a while
    for _ in range(1000): 
        curr = findMinCut(deepcopy(G)) # make a deepcopy of G in every iteration
        if curr < mincut:
            mincut = curr
    print("The min cut is:", mincut)

if __name__ == '__main__':
    main()
