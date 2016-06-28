'''
alternative approach
dissassemble the subject.
construct less and greater arrays.
if the middle component of subject is bigger than query, move left half into less
if the middle component of subject is smaller than query, move the right half into greater
if the middle component equals the query, return middle index + length of less

'''
def chop(query, subject):
    less = []
    greater = []
    candidates = subject
    while candidates:
        check = len(candidates)//2
        value = candidates[check]
        if value == query:
            return check + len(less)
        if len(candidates) == 1:
            return -1
        if value < query:
            less += candidates[:check]
            candidates = candidates[check:]
        if value > query:
            greater = candidates[check:] + greater
            candidates = candidates[:check]
    return -1

'''
errors:
    runs on the first try and passes surprising number of tests.
    fails to find first element in collection
    the 1-element failure mode was prematurely triggering.
salamanders
angelo + erin: refresh basics, strings vs symbols vs variable names
david + bahman: want more references
'''
