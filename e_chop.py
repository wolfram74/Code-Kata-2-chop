'''
informed recursive chop:
much like informed chop but instead a recursive implementation
'''
def chop(query, subject):
    if len(subject) == 0:
        return -1
    if subject[0] > query or subject[-1] < query:
        return -1
    if subject[0] == query:
        return 0
    difference = subject[-1] - subject[0]
    max_index = len(subject)-1
    check = int(max_index*(query-subject[0])/difference)
    test = subject[check]
    if test == query:
        return check
    elif test > query:
        sub_result = chop(query, subject[:check])
        if sub_result == -1:
            return -1
        return sub_result
    else :
        sub_result = chop(query, subject[check+1:])
        if sub_result == -1:
            return -1
        return sub_result+check+1
'''
errors:
    first draft compiles and looking left isn't really working, it seems.
    apparently negative indexing worked differently than I expected.
    infinite recursion.
    fixed infinite recursion and out of indexing problem.
'''
