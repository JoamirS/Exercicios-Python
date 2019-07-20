'''
    Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
    o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
    entre eles(desconsiderando o flag).
'''

NumberCondition = 0
NumberCount = 0
NumberSecond = 0

while NumberCondition != 999:
    NumberFirst = int(input('Digite um número inteiro: '))
    NumberSum = NumberFirst + NumberSecond
    NumberSecond = NumberSum
    NumberCount += 1
    NumberCondition = int(input('Tecle [999] para sair | Tecle [1] para continuar: '))
print('O número de números digitados foi {} e a soma entre eles foi {} '.format(NumberCount, NumberSum))

