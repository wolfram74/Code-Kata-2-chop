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
    if len(subject) == 0:
        return -1
    middle = len(subject)//2
    test = subject[middle]
    if test == query:
        return middle
    elif test > query:
        sub_result = chop(query, subject[0:middle])
        if sub_result == -1 : return -1
        return sub_result
    else:
        sub_result = chop(query, subject[middle:-1])
        if sub_result == -1 : return -1
        return sub_result+(middle-1)
    return -1
'''
erros:
    syntax error
    one out of index error and 2 off by one errors.
    undefined variable error
    now only off by 1 errors.
    I didn't take into account that the middle index was getting over counted. I noticed it writing it, but wasn't sure exactly how to account for it.
    actually, still broken, and larger subjects misbehaving as well.
    wow, returning query instead of index? ya doof.
'''
