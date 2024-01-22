"""
os.path.getsize
"""

import math
import os
from itertools import count


def format_size(size_in_bytes, base: int = 1_000):

    if size_in_bytes <= 0:
        return "0B"

    abbreviation_sizes = "B", "KB", "MB", "GB", "TB", "PB"
    '''
    math.log will return the logarithm of size_in_bytes with the base (1024 for default), this should match our index of
    abbreviation of sizes.
    '''
    index_abbreviation_sizes = int(math.log(size_in_bytes, base))
    '''
    By how much should it be divided for generate the correct size.
    '''
    power = base ** index_abbreviation_sizes
    # Our final size
    final_size = round(size_in_bytes / power, 2)
    # Abbreviation we want
    abbreviation_size = abbreviation_sizes[index_abbreviation_sizes]
    return f'{final_size} {abbreviation_size}'


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
        complete_file_path = os.path.join(root, file)
        size = os.path.getsize(complete_file_path)
        print('   ', the_counter, 'FILE: ', file, format_size(size))


print(format_size(10000))
