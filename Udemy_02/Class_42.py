"""
Recursive function and recursion
Functions that can be called back
Useful for breaking up large problems and smaller parts
Every recursive function must be:
- A problem can be breaking up in smaller parts
- A recursive case that solve a little problem
- A base case for the recursion
"""


def recursive(begin=0, end=4):
    print(begin, end)
    if begin >= end:
        return end
    begin += 1
    return recursive(begin, end)


print(recursive())
