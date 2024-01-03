# Unindo caminhos
import os

file_path = os.path.join('\\home\\users', 'Desktop', 'curso', 'file.txt')
print(file_path)
path, file = os.path.split(file_path)
print(path)
file_path_two, file_extension = os.path.splitext(file)
print(file_path_two)
print(file_extension)

print(os.path.exists(file_path))
print(os.path.exists('C:\\Users\\joami\\Documents\\Curso Python\\Python_A-Z\\Python_04'))
print(os.path.abspath('.'))
print(os.path.basename(file_path))
