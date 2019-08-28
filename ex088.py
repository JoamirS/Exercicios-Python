"""
    Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão
    gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep

ListGuess = []
ListGuessTemporary = []

print('_' * 30)
print('         JOGUE NA MEGA SENA        ')
print('_' * 30)

HowManyTimesPlay = int(input('Quantos jogos você quer sortear? '))
CountTimesLoop = 1
while CountTimesLoop <= HowManyTimesPlay:
    SixNumberCounter = 0
    while True:
        NumberFromOneToSixty = randint(1, 60)
        if NumberFromOneToSixty not in ListGuessTemporary:
            ListGuessTemporary.append(NumberFromOneToSixty)
            SixNumberCounter += 1
        if SixNumberCounter >= 6:
            break

    ListGuessTemporary.sort()
    ListGuess.append(ListGuessTemporary[:])
    ListGuessTemporary.clear()

    CountTimesLoop += 1
print('-' * 3, 'Sorteando {} jogos.'.format(HowManyTimesPlay), '-' * 3)
for PositionList, ExtractedNumbersOfList in enumerate(ListGuess):
    print('Jogo {}: Os números sorteados foram {}'.format(PositionList + 1, ExtractedNumbersOfList))
    sleep(2)

