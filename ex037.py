"""
    Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
    1 para binário | 2 para octal | 3 para hexadecimal
"""
numberInput = int(input('Digite um número inteiro: '))
print(''' Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
optionInput = int(input('Sua opção: '))
if optionInput == 1:
    print(f'{numberInput} convertido para BINÁRIO é igual a {bin(numberInput)[2:]}')
elif optionInput == 2:
    print(f'{numberInput} convertido para OCTAL é igual a {oct(numberInput)[2:]}')
elif optionInput == 3:
    print(f'{numberInput} convertido para HEXADECIMAL é igual a {hex(numberInput)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
