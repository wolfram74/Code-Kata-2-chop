'''
iterative solution for binary search of list length N:
start with two posts, 0 and N-1, low(bound) and high(bound)
low and high average to check
set test to value at index check
if test == query, return check
if test < query, set low to check+1
if test > query, set high to check-1
continue until low >= high, if that point is reached, return -1
'''
def chop(query, subject):
    return -1
