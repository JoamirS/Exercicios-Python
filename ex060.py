'''
    Faça um programa que leia um número qualquer e calcule seu fatorial
'''
# Declarando minhas variáveis
NumberOne = int(input('Digite o número desejado: '))
NumberCount = NumberOne
NumberFactorial = 1
# Criando meu laço de repetição

while NumberCount > 0:
    NumberFactorial *= NumberCount
    NumberCount -= 1
print('O fatorial de {} é {}'.format(NumberOne, NumberFactorial))
