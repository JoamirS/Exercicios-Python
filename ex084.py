"""
    Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas
    pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.
"""
ListNameAndWeight = []
TemporaryList = []
CountNumberPeopleRegistered = 0
HigherWeight = 0
LessWeight = 0

while True:
    TemporaryList.append(str(input('Digite seu nome: ')))
    TemporaryList.append(int(input('Digite sua peso: ')))

    if len(ListNameAndWeight) == 0:
        HigherWeight = TemporaryList[1]
        LessWeight = TemporaryList[1]
    else:
        if TemporaryList[1] > HigherWeight:
            HigherWeight = TemporaryList[1]
        if TemporaryList[1] < LessWeight:
            LessWeight = TemporaryList[1]

    ListNameAndWeight.append(TemporaryList[:])
    TemporaryList.clear()

    CountNumberPeopleRegistered += 1

    ConditionalInputBreak = str(input('Deseja continuar digitando? \nSim ou Não: ')).strip().upper()[0:3]
    while ConditionalInputBreak not in 'SIMNÃO':
        ConditionalInputBreak = str(input('Deseja continuar digitando? \nSim ou Não: ')).strip().upper()[0:3]
    if ConditionalInputBreak == 'NÃO':
        break


print('O maior peso foi {}. Que foi o peso de: '.format(HigherWeight), end='')
for PersonNameHigherWeight in ListNameAndWeight:
    if PersonNameHigherWeight[1] == HigherWeight:
        print('{}'.format(PersonNameHigherWeight[0]))


print('O menor peso foi {}. Que foi o peso de: '.format(LessWeight), end='')
for PersonNameLessWeight in ListNameAndWeight:
    if PersonNameLessWeight[1] == LessWeight:
        print('{}'.format(PersonNameLessWeight[0]), end=', ')

print('\nVocê cadastratou {} pessoas'.format(CountNumberPeopleRegistered))
