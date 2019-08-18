"""
    Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
    correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

ListNumbers = []
CountNumberInput = 0

for CountFromOneToFive in range(0, 5):
    CountNumberInput += 1
    InputNumbersZeroToFive = (int(input('Digite o {}º número: '.format(CountNumberInput))))

    if CountFromOneToFive == 0 or InputNumbersZeroToFive > ListNumbers[-1]:
        ListNumbers.append(InputNumbersZeroToFive)
        print('Número adicionado no final da lista, na 5ª posição')

    else:
        PositionNumberInList = 0
        while PositionNumberInList < len(ListNumbers):
            if InputNumbersZeroToFive <= ListNumbers[PositionNumberInList]:
                ListNumbers.insert(PositionNumberInList, InputNumbersZeroToFive)
                print('Adicionado na posição {} da lista'.format(PositionNumberInList))
                break
            PositionNumberInList += 1


print('Os valores digitados foram {}'.format(ListNumbers))