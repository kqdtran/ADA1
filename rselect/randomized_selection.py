# Algorithms: Design and Analysis Part 1, Coursera
# Week 3 Material: Randomized Selection of an array/list in linear time.

from random import randint

def partition(lst, start, end):
    """Partition the array/list lst around a certain pivot choosing uniformly at random
    lst = input list/array
    start = start index
    end = end index"""

    random_index = randint(start, end)
    lst[start], lst[random_index] = lst[random_index], lst[start] # swap random with first element to begin the partition method
    pivot = lst[start]
    i = start + 1
    for j in range(start+1, end+1): # indices from start+1 to end
        if lst[j] < pivot:
            lst[j], lst[i] = lst[i], lst[j]
            i += 1
    lst[start], lst[i-1] = lst[i-1], lst[start]
    return i-1

def rselect(lst, k):
    """Return the randomized selection of the kth order statistics in the input list
    lst = originial input list
    ostats = order statistics k, or kth smallest element in the original list"""
    k -= 1 # take into account that index actually starts at 0
    if len(lst) == 1: # base case return sole element
        return lst[0]
    pivot_index = partition(lst, 0, len(lst)-1)
    if pivot_index == k:
        return lst[pivot_index]
    elif pivot_index > k:
        return rselect(lst[:pivot_index], k+1)
    else:
        return rselect(lst[(pivot_index+1):], k-pivot_index)
    
def main():
    count = [0] # a mutable data struct for counting the number of inversions
    f = open('RSelectTest.txt', 'r')
    line_list = f.readlines()
    int_list = [int(line.split()[0]) for line in line_list if line] 
    print(rselect(int_list, 8)) # desired 8th smallest element

if __name__ == '__main__':
    main()
