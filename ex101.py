"""
    Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira
    função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os
    valores PARES sorteados pela função anterior.
"""

from random import randint
NumbersList = list()
ListNumbersEven = list()
ListSumNumbersEven = list()


def sorteia(TotalNumbersDrawn):
    CounterTotalLoopDraw = TotalNumbersDrawn
    while CounterTotalLoopDraw > 0:
        NumberDrawn = randint(0, 100)
        NumbersList.append(NumberDrawn)
        if NumberDrawn % 2 == 0:
            ListNumbersEven.append(NumberDrawn)
        CounterTotalLoopDraw -= 1


InputUser = int(input('Quantos números você quer sortear? '))
sorteia(InputUser)
print(NumbersList)


def somaPar(EvenNumbers):
    SumAllNumbersEven = 0
    for Number in EvenNumbers:
        SumAllNumbersEven += Number
    ListSumNumbersEven.append(SumAllNumbersEven)


somaPar(ListNumbersEven)
print('Somando os valores pares de {}, o resultado é {}'.format(NumbersList, ListSumNumbersEven))
