'''
informed chop:
inspect the index that would be the result of a roughly even spacing of values based on the first and last value.
'''

def chop(query, subject):
    low = 0
    high = len(subject)-1
    while low <= high:
        difference = subject[high] - subject[low]
        index_range = high-low
        if index_range != 0:
            index_gap = difference/index_range
            check = int(low + (query-subject[low])/index_gap)
        else:
            check = low
        if check < low:
            break
        test = subject[check]
        if test == query: return check
        if test < query:
            low = check + 1
        else:
            high = check - 1
    return -1
'''
errors, once I got the infinite loop stopping, it passed all tests first try.
Had forgotten the case where query was not present, in which case it would be possible for check to be less than the lower bound.
'''
