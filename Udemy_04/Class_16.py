"""
os + shutil - Move, Copy and delete files
Move/Rename -> shutil.move
Move/Rename -> os.rename
copy -> os.unlink
delete -> os.unlink
"""

import os
import shutil

HOME = os.path.expanduser('~')
print(HOME)

DESKTOP = os.path.join(HOME, 'Desktop')
original_folder = os.path.join(DESKTOP, 'EXEMPLO')
new_folder = os.path.join(DESKTOP, 'Nova_pasta')

os.makedirs(new_folder)

for root, dirs, files in os.walk(original_folder):
    for file in files:
        print(file)
