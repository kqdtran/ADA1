# Algorithms: Design and Analysis Part 1, Coursera
# Week 6 Problem A: Variant of the Two-Sum Problem
# The file contains 500,000 positive integers (there might be some repetitions!).
# Compute the number of target values t in the interval [2500,4000] (inclusive)
# such that there are distinct numbers x, y in the input file that satisfy x+y=t.

import sys

def make_dict(filename):
    """Read in the data stored in the text file and store them into a hash table (Python's dictionary)
    Input: filename - the name of the text file"""

    try: 
        f = open(filename, 'r')
    except IOError:
        sys.exit("No such file!")
    line_list = f.readlines()
    dic = {(int)(elem) for elem in line_list}
    return dic

def findNumTwoSum(dic):
    """Compute the number of target values t in the interval [2500,4000] (inclusive)
    such that there are distinct numbers x, y in the input file that satisfy x+y=t.
    
    Input: dic - a hash table contains all the numbers in the input file"""

    numSatisfied = 0 # the number of target values that passed the requirement
    for target in range(2500, 4001): # [2500, 4000]
        for x in dic:
            y = target - x
            if y in dic and y != x: # ensure dictinctness
                numSatisfied += 1
                break
    return numSatisfied
    
def main():
    dic = make_dict("HashInt.txt")
    print("The number of target values in [2500, 4000] that satisfied the requirement is:", \
              findNumTwoSum(dic))
    
if __name__ == '__main__':
    main()
