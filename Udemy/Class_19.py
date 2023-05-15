"""
Introduction to unpacking + tuples
"""

# name_01, name_2 = ['Maria', 'Helena', 'Luiz']

'''
The asterisk indicate to ignore the rest of list when the variable isn't the same len of attributes and save the 
rest in another variable
'''
name, *_ = ['Maria', 'Helena', 'Luiz']
print(name)
print(_)

