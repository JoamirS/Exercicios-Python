# Manage folders and write file | append mode

file_path = 'class_45.txt'

with open(file_path, 'a+') as file:
    file.write('Line one\n')
    file.write('Line two\n')
    file.write('Line three\n')