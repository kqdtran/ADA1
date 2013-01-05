# Algorithms: Design and Analysis Part 1, Coursera
# Week 6 Problem B: Median Maintenance
# Find the sum of all the medians of a stream of integers, arriving one by one, 
# , each in O(log i) time, with i denoting the number of integers processed so far

import sys
from heapq import heappush, heappop
from stream import Stream

def read_file(filename):
    """Read in the data stored in the text file and store them into a list
    Input: filename - the name of the text file"""

    try: 
        f = open(filename, 'r')
    except IOError:
        sys.exit("No such file!")
    line_list = f.readlines()
    lst = [elem.rstrip('\n') for elem in line_list] # remove trailing newline character
    return lst
    
def make_stream(lst):
    """Make a stream of integers from a pre-populated list of integers
    Input: lst - a list of integers"""

    if not lst:
        return None
    def compute_rest():
        return make_stream(lst[1:])
    return Stream(lst[0], compute_rest)

def compute_median(s):
    """Compute the current median of the stream s in O(log i) time.
    We achieve that by using a min heap for the top half of the elements,
    and a max heap for the bottom half

    Since Python's heapq is implemented as a min heap, we have to 
    negate (*-1) all of the elements to make it work as a max heap

    Step 1: Add next item to one of the heaps. If next item is smaller than 
    maxHeap root add it to maxHeap, else add it to minHeap

    Step 2: Balance the heaps (after this step heaps will be either balanced or
    one of them will contain 1 more item). If number of elements in one of the heaps 
    is greater than the other by more than 1, remove the root element from the one 
    containing more elements and add to the other one

    Step 3: Compute the median. If the number of elements is odd (i.e. one of the heap is
    bigger than the other), it's the root of the bigger heap. Else, it's the root of the
    max heap(lower_half) since we want the kth/2 smallest element as the median.
    
    Input: s - a stream of integers"""
    
    upper_half, lower_half = [], [] # initialize the min and max heap respectively
    while s: # while the stream is not empty
        # If lower_half is initially empty or
        # the first element of the stream is smaller than the max of lower_half
        if len(lower_half) == 0 or (int)(s.first) < -(lower_half[0]): 
            heappush(lower_half, -(int)(s.first)) 
        else:
            heappush(upper_half, (int)(s.first))
        s = s.rest # advance the stream one element further

        # rebalance step
        if len(upper_half) - len(lower_half) > 1:
            heappush(lower_half, -heappop(upper_half))
        elif len(lower_half) - len(upper_half) > 1:
            heappush(upper_half, -heappop(lower_half))

        # now compute the median
        if len(upper_half) > len(lower_half):
            yield upper_half[0]
        else:
            yield (-lower_half[0])
            
def main():
    lst = read_file("Median.txt")
    s = make_stream(lst)
    final_sum = 0
    for median in compute_median(s):
        final_sum += median
    print("Sum of all the medians modulo 10000 is:", final_sum % 10000)

if __name__ == '__main__':
    main()
