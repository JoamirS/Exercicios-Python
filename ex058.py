'''
    Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador
    vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

    Recapitulando o exercício 028...
      Faça um programa que faça o computador 'Pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar
      descobrir qual foi o número escolhido pelo computador.
            O programa deverá escrever na tela se o usuário venceu ou perdeu.
            ----- Outra maneira de declarar a variável
            ------ from randon import randit
            ------ computador = randit(0, 5) | Coloca-se o intervalo em que se buscar uma informação
            ------ print('Pensei no número {}'.format(computador)
'''
# Importando o módulo de escolha aleatória
from random import choice
NumberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
SystemChoice = choice(NumberList)
PlayerChoice = int(input('Digite um número de 1 até 10: '))
NumberCount = 0

while PlayerChoice != SystemChoice:
    PlayerChoice = int(input('Tentativa errada, o número não é esse. Tente outro número: '))
    NumberCount += 1
else:
    print('Parabéns você acertou o número!')
    print('Para você acertar, foram necessários {} palpites'.format(NumberCount))
