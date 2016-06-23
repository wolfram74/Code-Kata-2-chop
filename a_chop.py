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
    low = 0
    high = len(subject)-1
    while low <= high:
        check = int((low + high)/2)
        test = subject[check]
        if test == query: return check
        if test < query:
            low = check + 1
        else:
            high = check - 1
    return -1
'''
errors encountered:
    typo with higher
    check got turned into a float
    all instances failed, results return -1
    in the case of array length 1 it would automatically skip to the end. Why that caused the other lengths to fail is curious.
'''
