'''
    Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
    No final, mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista.
'''

NumberCountInputUser = 1
NumberList = []

for InputsUser in range(0, 5):
    NumberList.append(int(input('Digite o {}º valor: '.format(NumberCountInputUser))))
    NumberCountInputUser += 1
print('A lista formada após os valores digitados foi {}'.format(NumberList))


print('O maior valor digitado foi {}, na posição '.format(max(NumberList)), end='')
for PositionHighest, ElementsListHigh in enumerate(NumberList):
    if ElementsListHigh == max(NumberList):
        print('{},'.format(PositionHighest), end='')


print('\nO menor valor digitado foi {}, na posição '.format(min(NumberList)), end='')
for PositionLower, ElementsListLower in enumerate(NumberList):
    if ElementsListLower == min(NumberList):
        print('{},'.format(PositionLower), end='')
