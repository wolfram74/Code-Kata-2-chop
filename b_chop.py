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
    if len(subject) == 1 and subject[0] != query:
        return -1
    middle = len(subject)//2
    test = subject[middle]
    if test == query:
        return middle
    elif test > query:
        sub_result = chop(query, subject[:middle])#front half
        if sub_result == -1:
            return -1
        return sub_result
    else :
        sub_result = chop(query, subject[middle:])#back half
        if sub_result == -1:
            return -1
        return sub_result+middle #keep in mind what we saw before
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
    generally things not working on moving right. Not even being found.
    after fixing a lot of the edge case problems, removed the off by one "fix", because it was actually ruining things.
    This works, I wrote it, and I'm still not very clear on how it works.
'''
