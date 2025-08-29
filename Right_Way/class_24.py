"""
 Exercises list
"""
'''
Make a program read two strings and display their contents followed your self weight.
Also report whether the two strings are the same length and have the same or different content.
'''

first_string = input('Digite a string 1: ')
second_string = input('Digite a string 2: ')

print(f'String 1: {first_string}')
print(f'String 2: {second_string}')

print(f"O tamanho de '{first_string}' é: {len(first_string)}")
print(f"O tamanho de '{second_string}' é: {len(second_string)}")

if len(first_string) == len(second_string):
    print('As strings possuem o mesmo tamanho.')
else:
    print('As strings possuem tamanhos diferentes.')

if first_string == second_string:
    print('As duas strings possuem conteúdos iguais.')
else:
    print('As duas strings possuem conteúdos diferentes.')
