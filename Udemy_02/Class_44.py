# Manage folders and write file

file_path = 'class_44.txt'

with open(file_path, 'w+') as file:
    file.write('Line one\n')
    file.write('Line two\n')
    file.write('Line three\n')
    file.writelines(
        ('Linha 4\n', 'Linha 5\n')
    )
    file.seek(0, 0)
    print(file.read())
    file.seek(0, 0)
    print(file.readline(6))
    print(file.readline())

    print('READLINES')
    file.seek(0, 0)
    for line in file.readlines():
        print(line.strip())

print('#' * 10)

with open(file_path, 'r') as file:
    print(file.read())
