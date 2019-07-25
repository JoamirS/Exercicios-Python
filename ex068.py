'''
    Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
    mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import choice
CountNumberWinsPlayer = 0
while True:
    print('-' * 25)
    print('Vamos jogar par ou ímpar!')
    print('-' * 25)
    # Entradas do usuário
    NumberChoicePLayer = int(input('Diga um número: '))
    ChoicePlayerEvenOrOdd = str(input('Digite par ou ímpar: ')).upper()
    # Condições para a escolha do sistema
    if ChoicePlayerEvenOrOdd == 'ÍMPAR':
        ChoiceSystemEvenOrOdd = 'PAR'
    elif ChoicePlayerEvenOrOdd == 'PAR':
        ChoiceSystemEvenOrOdd = 'ÍMPAR'
    else:
        print('Você só pode digitar par ou ímpar!\n Tente novamente')
        break
    # Escolhas do sistema
    ListNumbers1to10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ChoiceSystem = choice(ListNumbers1to10)

    # Operações com os números escolhidos
    SumNumbersChoices = NumberChoicePLayer + ChoiceSystem
    if SumNumbersChoices % 2 == 0:
        SumNumberEvenOrOdd = 'PAR'
    else:
        SumNumberEvenOrOdd = 'ÍMPAR'

    print(f'Você jogou {NumberChoicePLayer} e o sistema {ChoiceSystem} e a soma entre eles foi de {SumNumbersChoices}')
    print(f'O total deu {SumNumbersChoices}, e este número é {SumNumberEvenOrOdd}')
    if SumNumberEvenOrOdd != ChoiceSystemEvenOrOdd:
        CountNumberWinsPlayer += 1
    else:
        break
print(f'Você conquistou {CountNumberWinsPlayer} vitórias')
