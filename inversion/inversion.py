# Algorithms: Design and Analysis Part 1, Coursera
# Problem 1: Counting the number of inversions in O(nlogn) time
# This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some random order, with no integer repeated. Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.

def count_inversion(li, c):
    """Count the number of inversions in O(nlogn) time
    li = the original list
    c = a mutable data struct to store the number of inversions"""
    
    length = len(li)
    if length < 2:
        return li
    else:
        middle = int(length / 2)
        return count_split_inversion(count_inversion(li[:middle], c), \
                                     count_inversion(li[middle:], c), c)

def count_split_inversion(left, right, c):
    """Count the number of split inversions, i.e. inversions that occur in both halves of the array.
    left = the left sorted list
    right = the right sorted list
    c = a mutable data struct to store the number of inversions"""
    
    result = []
    while left and right:
        curr = left if left[0] < right[0] else right
        result.append(curr.pop(0))
        if curr == right:
            c[0] += len(left)
    result.extend(left if left else right)
    return result
        
def main():
    count = [0] # a mutable data struct for counting the number of inversions
    f = open('IntegerArray.txt', 'r')
    line_list = f.readlines()
    int_list = [int(line.split()[0]) for line in line_list if line] 
    count_inversion(int_list, count)
    print(count[0])

if __name__ == '__main__':
    main()
