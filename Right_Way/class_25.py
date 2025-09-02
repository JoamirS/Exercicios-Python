"""
Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste
 conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.
"""

input_cellphone_number = input('Digite seu número: ')

modified_string = input_cellphone_number.replace('-', '')

print(modified_string)

if len(modified_string) == 7:
    print('3' + modified_string)
else:
    print('O telefone não tem 7 dígitos.')
