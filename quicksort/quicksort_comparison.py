# Algorithms: Design and Analysis Part 1, Coursera
# Problem 2: Find the number of comparisons in quicksort in three different pivot-selecting ways: first index, last index, and median of three, respectively
# For this problem, assume way 0 = first index element as pivot, 1 = last as pivot, 2 = median of three as pivot

def median_of_three(lst, start, end):
    """Returns the index of the median of three values: the first one, the last one, and the middle one.
    lst = input list/array
    start = start index
    end = end index"""

    middle = start + int((end - start) / 2)
    median = min(max(lst[start], lst[end]),
                 max(lst[start], lst[middle]),
                 max(lst[middle], lst[end]))
    if median == lst[start]:
        return start
    elif median == lst[end]:
        return end
    else:
        return middle
        
def partition(lst, start, end, num_comparison, way):
    """Partition the array/list lst around a certain pivot choosing by way
    lst = input list/array
    start = start index
    end = end index
    num_comparison = mutable data struct to store the number of comparisons
    way = which way to select the pivot"""

    if way == 1:
        lst[end], lst[start] = lst[start], lst[end] # exchange last and first
    elif way == 2:
        median_of_three_index = median_of_three(lst, start, end)
        lst[median_of_three_index], lst[start] = lst[start], lst[median_of_three_index]
    else:
        assert way == 0, "Illegal pivot selection way"

    pivot = lst[start]
    i = start + 1
    num_comparison[0] += end - start
    for j in range(start+1, end+1): # indices from start+1 to end
        if lst[j] < pivot:
            lst[j], lst[i] = lst[i], lst[j]
            i += 1
    lst[start], lst[i-1] = lst[i-1], lst[start]
    return i-1

def quicksort(lst, start, end, num_comparison, way=0):
    """The quicksort algorithm which runs in O(nlogn) time on average
    lst = input list/array
    start = start index
    end = end index
    num_comparison = mutable data struct to store the number of comparisons
    way = which way to select the pivot"""

    if start < end: # if list has 2 or more items
        pivot_index = partition(lst, start, end, num_comparison, way)
        quicksort(lst, start, pivot_index-1, num_comparison, way)
        quicksort(lst, pivot_index+1, end, num_comparison, way)

def main():
    print("Assume 0 = first index, 1 = last index, 2 = median of three as pivot-selection method")
    for way in range(3): # 0, 1, and 2
        f = open('QuickSort.txt', 'r')
        line_list = f.readlines()
        int_list = [int(line.split()[0]) for line in line_list if line]
        num_comparison = [0]
        quicksort(int_list, 0, len(int_list)-1, num_comparison, way)
        print("The number of comparisons in way {0} is".format(way), num_comparison[0])
    
if __name__ == '__main__':
    main()
