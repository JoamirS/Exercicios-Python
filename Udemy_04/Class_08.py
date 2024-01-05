import os

file_path = os.path.join(r'C:\\Users\\joami\\Documents\\Curso Python\\Python_A-Z')

for directory in os.listdir(file_path):
    if not os.path.isdir(directory):
        continue

    for image in os.listdir(directory):
        print(image)
