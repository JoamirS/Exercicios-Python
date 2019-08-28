"""
    Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a
    matriz na tela, com a formatação correta.
"""
ListMatrix = []
CountLine = 1
CountColumn = 0
CountInsertValue = 1

while CountInsertValue < 10:
    if CountColumn < 3:
        CountColumn += 1
    else:
        CountColumn -= 2
        CountLine += 1

    InputUserValueMatrix = int(input('Digite o valor da linha {} e coluna {}: '.format(CountLine, CountColumn)))

    ListMatrix.append(InputUserValueMatrix)

    CountInsertValue += 1

print('Sua matrix 3x3 é :')
print('-' * 25)
print(f'{ListMatrix[0]} | {ListMatrix[1]} | {ListMatrix[2]}')
print(f'{ListMatrix[3]} | {ListMatrix[4]} | {ListMatrix[5]}')
print(f'{ListMatrix[6]} | {ListMatrix[7]} | {ListMatrix[8]}')
