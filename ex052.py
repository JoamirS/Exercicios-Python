"""
    Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
    Como dois é o único número primo par, foi feito um if só para este número.
"""

number = int(input('Digite um número inteiro: '))
if number == 2:
    print('2 é um número primo. Ele é divisível por 1 e por ele mesmo.')
totalNumberDivisors = 0
for c in range(1, number + 1):
    if number % c == 0:
        print('\033[34m', end='')
        totalNumberDivisors += 1
    else:
        print('\033[33m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(number, totalNumberDivisors))
if totalNumberDivisors == 2:
    print('Por isso ele é um número primo.')
else:
    print('E por isso ele não é primo.')