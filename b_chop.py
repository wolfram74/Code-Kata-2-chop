'''
recursive solution to binary:
at each level, check the middle element (N/2)
if check < query,
    recurse on right half
    and add length of left half to result
    pass to next level
if check > query,
    recurse on left half.
    pass up result
base case, an array length 1 that has the query in it, or an empty array.
if an empty array, return -1
if present, return 0.
'''

def chop(query, subject):
    middle = len(subject)//2
    test = subject[middle]
    if test == query:
        return query
    elif test > query:
        sub_result = chop(query, subject[0:middle])
        if sub_result == -1 : return -1
        return sub_result
    else
        if sub_result == -1 : return -1
        sub_result = chop(query, subject[middle:-1])
        return sub_result+middle
    return -1
