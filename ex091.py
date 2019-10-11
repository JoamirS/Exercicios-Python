"""
    Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
    dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from operator import itemgetter
from random import randint
from time import sleep

RankingDice = dict()
ChoicePlayersDictionary = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6),
                           'Jogador 4': randint(1, 6)}
print('Valores sorteados: ')
for Keys, Values in ChoicePlayersDictionary.items():
    print('{} tirou {} no dado.'.format(Keys, Values))
    sleep(1)

print('-' * 30)
RankingDice = sorted(ChoicePlayersDictionary.items(), key=itemgetter(1), reverse=True)

for PositionLocation, ValuesRanking in enumerate(RankingDice):
    print('{}º lugar: {} com {}'.format(PositionLocation + 1, ValuesRanking[0], ValuesRanking[1]))
