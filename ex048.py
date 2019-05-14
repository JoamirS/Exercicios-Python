'''
    Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram
    no intervalo de 1 até 500.
'''
#   Declarando as varíaveis
sumNumbers = 0
counterNumbers = 0
#   Declarando o laço, contando de 1 a 500, só com números ímpares e múltiplos de 3.
for c in range(1, 501, 2):
    if c % 3 == 0:
        counterNumbers = counterNumbers + 1
        sumNumbers = sumNumbers + c
print('A soma de todos os {} valores solicitados é {}'.format(counterNumbers, sumNumbers))
