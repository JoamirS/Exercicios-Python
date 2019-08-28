"""
    Aprimore o desafio anterior, mostrando no final:
    A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda
    linha.
"""

ListMatrix = []
ListSecondLine = []
ListEvenNumbers = []
BiggerNumberSecondLine = 0
CountColumn = 0
CountInsertValue = 1
CountLine = 1
SumNumbersEven = 0
SumNumbersThirdColumn = 0

while CountInsertValue < 10:
    if CountColumn < 3:
        CountColumn += 1
    else:
        CountColumn -= 2
        CountLine += 1

    InputUserValueMatrix = int(input('Digite o valor da linha {} e coluna {}: '.format(CountLine, CountColumn)))

    if InputUserValueMatrix % 2 == 0:
        ListEvenNumbers.append(InputUserValueMatrix)
        SumNumbersEven = sum(ListEvenNumbers)

    ListMatrix.append(InputUserValueMatrix)

    CountInsertValue += 1

ListSecondLine.append(ListMatrix[3])
ListSecondLine.append(ListMatrix[4])
ListSecondLine.append(ListMatrix[5])
BiggerNumberSecondLine = max(ListSecondLine)

SumNumbersThirdColumn = ListMatrix[2] + ListMatrix[5] + ListMatrix[8]

print('Sua matrix 3x3 é :')
print('-' * 9, '|')
print(f'{ListMatrix[0]} | {ListMatrix[1]} | {ListMatrix[2]}')
print(f'{ListMatrix[3]} | {ListMatrix[4]} | {ListMatrix[5]}')
print(f'{ListMatrix[6]} | {ListMatrix[7]} | {ListMatrix[8]}')
print('-' * 9, '|')
print('A soma de todos os valores pares é {}'.format(SumNumbersEven))
print('A soma dos valores da terceira coluna é {}'.format(SumNumbersThirdColumn))
print('O maior valor da segunda linha é {}'.format(BiggerNumberSecondLine))
