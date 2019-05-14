'''
    Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o
    valor digitado for ímpar, desconsidere-o.
'''
#Declarando as variáveis
sumNumber = 0
counterNumber = 0
#   Condição para os números de entrada
for c in range(1, 7):
    Number = int(input('Digite o {}º valor: '.format(c)))
    if Number % 2 == 0:
        sumNumber += Number
        counterNumber += 1
print('Você informou {} números pares e a soma foi {}.'.format(counterNumber, sumNumber))

