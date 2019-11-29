""" Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo. Seu
programa tem que realizar três contagens através da função criada:
    A) De 1 até 10, de 1 em 1
    B) De 10 até 0, de 2 em 2
    C) Uma contagem personalizada
"""


def counter(StartNumber, EndNumber, StepNumber):
    if StartNumber < EndNumber:
        while StartNumber <= EndNumber:
            print(StartNumber, end=' ')
            StartNumber += StepNumber
    elif StartNumber > EndNumber:
        while StartNumber >= EndNumber:
            print(StartNumber, end=' ')
            StartNumber -= StepNumber


counter(1, 10, 1)
print()
counter(10, 0, 2)
print()
StartNumberInput = int(input('Qual o número inicial da contagem? '))
EndNumberInput = int(input('Qual é o número final da contagem? '))
StepNumberInput = int(input('Qual é o valor da progressão? '))
counter(StartNumber=StartNumberInput, EndNumber=EndNumberInput, StepNumber=StepNumberInput)
