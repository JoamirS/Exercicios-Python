"""
    Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
    A) Quantos números foram digitados. | B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado se está ou não na lista.
"""
ListNumbers = []
CountNumberInput = 0
CountTimesNumber5Appear = 0
while True:
    InputNumberUser = int(input('Digite um valor para adicionar à lista: '))

    ListNumbers.append(InputNumberUser)

    CountNumberInput += 1

    if InputNumberUser == 5:
        CountTimesNumber5Appear += 1

    StopCondition = str(input('Deseja continuar digitando? \nSim ou Não: ')).upper().strip()[0:3]
    while StopCondition not in 'SIMNÃO':
        StopCondition = str(input('Deseja continuar digitando? \n Sim ou Não: ')).upper().strip()[0:3]

    if StopCondition == 'NÃO':
        break

ListNumbers.sort(reverse=True)

print('A quantidade de números digitados foi {}.'.format(CountNumberInput))
print('A lista ordenada de forma descrescente é {}.'.format(ListNumbers))
print('A quantidade que o número 5 aparece é de {} vezes.'.format(CountTimesNumber5Appear))

