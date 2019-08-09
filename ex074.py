'''
    Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois isso, mostre a listagem de
    números gerados e também indique o maior e o menor valor que estão na tupla.

    OBS: A variável TupleOneToTenFiveTimes é uma variável composta
'''

from random import randint

TupleOneToTenFiveTimes = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os números sorteados foram: ', end='')

for NumbersInTuple in TupleOneToTenFiveTimes:
    print(NumbersInTuple, end=' ')

print('\nO maior número entre os valores escolhidos é o {}'.format(max(TupleOneToTenFiveTimes)))

print('O menor número entre os valores escolhido é o {}'.format(min(TupleOneToTenFiveTimes)))
