"""
    Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
    conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
    listas geradas.
"""

ListAllNumbers = []
ListNumbersEven = []
ListNumbersOdd = []

while True:
    NumbersAddList = int(input('Digite um número: '))

    ListAllNumbers.append(NumbersAddList)

    if NumbersAddList % 2 == 0:
        ListNumbersEven.append(NumbersAddList)
    else:
        ListNumbersOdd.append(NumbersAddList)

    ConditionStop = str(input('Deseja continuar inserindo dados: Sim ou Não')).strip().upper()[0:3]
    while ConditionStop not in 'SIMNÃO':
        ConditionStop = str(input('Deseja continuar inserindo dados? Sim ou Não'))

    if ConditionStop == 'NÃO':
        break

print('A lista final com todos os valores digitados foi {}'.format(ListAllNumbers))
print('A lista final com todos valores pares foi de {}'.format(ListNumbersEven))
print('A lista final com todos os valores ímpares foi {}'.format(ListNumbersOdd))
