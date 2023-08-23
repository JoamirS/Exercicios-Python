# Manage folders

file_path = 'C:\\Users\\joami\\Documents\\Curso Python\\Python_A-Z\\Python_02\\'
file_path += 'Class_43.txt'
print(file_path)

# file = open(file_path, 'w')
#
# file.close()

with open(file_path, 'w') as file:
    print('Olá mundo')
    print('Seu arquivo vai ser fechado')
