import os

file_path = 'class_46.txt'

with open(file_path, 'a+') as file:
    file.write('Line one\n')
    file.write('Line two\n')
    file.write('Line three\n')

# os.remove(file_path) delete the file
os.rename(file_path, 'Class_46_b')

