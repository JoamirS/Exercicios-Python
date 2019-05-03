'''
    Crie um programa que faça o computador jogar Jokenpô com você.
'''
#Importando o módulo
from random import randint
from time import sleep
#Declarando as variáveis
items = ('Pedra','Papel', 'Tesoura')
print('Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEl\n[ 2 ] TESOURA')
computerChoice = randint(0, 2)
player = int(input('Qual é a sua jogada? '))
if player != 0 and player != 1 and player != 2:
    print('Jogada inválida. Tente outra vez.')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('Pô!!!!')
    sleep(1)
    print('-' * 27)
    print('Computador jogou {}'.format(items[computerChoice]))
    print('Jogador jogou {}'.format(items[player]))
    print('-' * 27)
    #Estruturas condicionais
    if computerChoice == 0: #Computador jogou PEDRA
        if player == 0:
            print('Resultado: Empate')
        elif player == 1:
            print('Resultado: Jogador vence')
        elif player == 2:
            print('Resultado: Computador vence')
        else:
            print('Jogada inválida!')
    elif computerChoice == 1: #Computador jogou PAPEL
        if player == 0:
            print('Resultado: Computador vence')
        elif player == 1:
            print('Resultado: Empate')
        elif player == 2:
            print('Resultado: Jogador vence')
        else:
            print('Jogada inválida!')
    elif computerChoice == 2: #Computador jogou TESOURA
        if player == 0:
            print('Resultado: Jogador vence')
        elif player == 1:
            print('Resultado: Computador vence')
        elif player == 2:
            print('Resultado: Empate')
        else:
            print('Jogada inválida!')
