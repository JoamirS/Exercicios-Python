"""
    Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
    exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
    crescente.
"""

ListNumbers = []
NumberCountInputUser = 1

while True:
    NumberAddList = int(input('Digite o {}º número: '.format(NumberCountInputUser)))

    while NumberAddList in ListNumbers:
        print('Este número já foi digitado na lista, escolha um número diferente.')
        NumberAddList = int(input('Digite o {}º número: '.format(NumberCountInputUser)))

    ListNumbers.append(NumberAddList)

    InputConditionalStopOrContinue = str(input('Deseja continuar? Sim ou Não')).strip().upper()[0:3]

    while InputConditionalStopOrContinue not in 'SIMNÃO':
        InputConditionalStopOrContinue = str(input('Deseja continuar? Sim ou Não')).strip().upper()[0:3]

    if InputConditionalStopOrContinue == 'NÃO':
        break

    NumberCountInputUser += 1

ListNumbers.sort()
print('A Lista construída pelos números digitados é: {}'.format(ListNumbers))
