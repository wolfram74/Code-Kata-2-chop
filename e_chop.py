'''
informed recursive chop:
much like informed chop but instead a recursive implementation
'''
def chop(query, subject):
    if len(subject) == 0:
        return -1
    if subject[0] > query or subject[-0] < query:
        return -1
    if subject[0] == query:
        return 0
    difference = subject[-0] - subject[0]
    length = len(subject)
    check = int(length*(query-subject[0])/difference)
    test = subject[check]
    print(check, subject)
    if test == query:
        return check
    elif test > query:
        sub_result = chop(query, subject[:check])
        if sub_result == -1:
            return -1
        return sub_result
    else :
        sub_result = chop(query, subject[check:])
        if sub_result == -1:
            return -1
        return sub_result+check
'''
errors:
    first draft compiles and looking left isn' really working, it seems.
'''
