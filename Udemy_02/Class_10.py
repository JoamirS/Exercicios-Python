"""
Type set
"""

set_one = set()
print(set_one)

set_two = {'Luiz', 1, 2, 3}
print(set_two)

'''
They are efficient to remove duplicate values of iterables
Your values always are uniques
They don't accept indexes
Do not guarantee order
They are iterables
'''

set_three = {1, 2, 3, 3, 3, 3, 3, 1}
print(set_three)

'''
useful operators:
    union |
    intersection &
    difference - Present items in left set
    symmetrical difference ^ Items not in both set (The inverse of the intersection)
'''

set_four = {1, 2, 3}
set_five = {2, 3, 4}
set_six = set_four | set_five
set_seven = set_four & set_five
set_eight = set_four - set_five
set_nine = set_four ^ set_five
print(set_nine)
