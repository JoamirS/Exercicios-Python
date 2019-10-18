""" Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
    quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
    guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

ListGoalsPerMatch = list()
SumGoalsPlayer = 0
CounterGoalsPerMatch = 1

NameSoccerPlayer = str(input('Qual é o nome do jogador? '))
PlayerMatches = int(input('Quantas partidas foram disputadas pelo jogador? '))
CounterPlayerMatches = PlayerMatches

CounterZeroToPlayerMatches = 1

while CounterPlayerMatches > 0:
    GoalsPerMatchPlayer = int(input('Quantos gols {} fez na partida {}: '.format(NameSoccerPlayer, CounterGoalsPerMatch)))
    CounterGoalsPerMatch += 1
    CounterPlayerMatches -= 1
    SumGoalsPlayer += GoalsPerMatchPlayer
    ListGoalsPerMatch.append(GoalsPerMatchPlayer)

    if CounterPlayerMatches == 0:
        break
print('--' * 30)
DictionaryPlayerInformation = {'Nome': NameSoccerPlayer, 'Gols': ListGoalsPerMatch, 'Total de gols': SumGoalsPlayer}
print(DictionaryPlayerInformation)
print('--' * 30)
for Key, Value in DictionaryPlayerInformation.items():
    print('O campo {} tem o valor {}'.format(Key, Value))

print('--' * 30)
print('O jogador {} jogou {} partidas.'.format(NameSoccerPlayer, PlayerMatches))
for CounterPosition, Value in enumerate(ListGoalsPerMatch):
    print('Na partida {}, fez {} gols.'.format(CounterPosition + 1, Value))

print('--' * 30)
print('Foi um total de {} gols'.format(SumGoalsPlayer))
