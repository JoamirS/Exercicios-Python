"""
os.walk

Is a way to permit walk through a structure of directories recursive way.
To give a tuple sequence, where each tuple has three elements: current directory, a list of subdirectories and a list of
file the current directory.
"""

import os
from itertools import count

file_path = os.path.join(r'C:\\Users\\joami\\Documents\\Curso Python\\Python_A-Z')
counter = count()

print(file_path)
print(counter)

for root, dirs, files in os.walk(file_path):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for directory in dirs:
        print('  ', the_counter, 'Dir: ', root)

    for file in files:
        print('   ', the_counter, 'FILE: ', file)
