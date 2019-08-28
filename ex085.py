"""
    Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
    mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

ListEvenOrOdd = []
ListEvenTemporary = []
ListOddTemporary = []
CountNumberInput = 0

for InputSevenNumbers in range(0, 7):
    CountNumberInput += 1
    InputNumberAddList = int(input('Digite o {}º número: '.format(CountNumberInput)))

    if InputNumberAddList % 2 == 0:
        ListEvenTemporary.append(InputNumberAddList)
    else:
        ListOddTemporary.append(InputNumberAddList)

    ListOddTemporary.sort()
    ListEvenTemporary.sort()

    ListEvenOrOdd.append(ListEvenTemporary)
    ListEvenOrOdd.append(ListOddTemporary)

print('Os valores pares foram {}'.format(ListEvenOrOdd[0]))
print('Os valores ímpares foram {}'.format(ListEvenOrOdd[1]))

