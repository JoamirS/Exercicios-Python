"""
    Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
    do aproveitamento de cada jogador.
"""

DictionaryPlayerInformation = dict()
ListPlayerFull = list()
ListPlayersInformation = list()
ListGoalsPerMatch = list()

while True:
    SumGoalsPlayer = 0
    CounterGoalsPerMatch = 1
    ListPlayersInformation.clear()
    ListGoalsPerMatch.clear()

    DictionaryPlayerInformation['Nome'] = str(input('Qual é o nome do jogador? '))
    PlayerMatches = int(input('Quantas partidas foram disputadas pelo {}? '.format(DictionaryPlayerInformation['Nome'])))
    CounterPlayerMatches = PlayerMatches

    while CounterPlayerMatches > 0:
        GoalsPerMatchPlayer = int(input('Quantos gols {} fez na partida {}: '.format(DictionaryPlayerInformation['Nome'], CounterGoalsPerMatch)))
        CounterGoalsPerMatch += 1
        CounterPlayerMatches -= 1
        SumGoalsPlayer += GoalsPerMatchPlayer
        ListGoalsPerMatch.append(GoalsPerMatchPlayer)

        if CounterPlayerMatches == 0:
            break

    print('--' * 30)
    DictionaryPlayerInformation['Gols'] = ListGoalsPerMatch[:]
    DictionaryPlayerInformation['Total de gols'] = SumGoalsPlayer

    print(DictionaryPlayerInformation)

    ListPlayersInformation.append(DictionaryPlayerInformation.copy())
    ListPlayerFull.append(ListPlayersInformation[:])

    StopCondition = str(input('Deseja continuar digitando? \nSim ou Não: ')).strip().upper()[0:3]
    while StopCondition not in 'SIMNÃO':
        StopCondition = str(input('Deseja continuar digitando? \nSim ou Não: ')).strip().upper()[0:3]
    if StopCondition == 'NÃO':
        break

print('ORDEM | NOME | GOLS POR PARTIDA | TOTAL DE GOLS')
for OrdinalNumber, InformationPlayer in enumerate(ListPlayerFull):
    print('{} | {:^10} | '.format(OrdinalNumber, InformationPlayer[0]['Nome']), end='')
    print(' {} | {:>3}'.format(InformationPlayer[0]['Gols'], InformationPlayer[0]['Total de gols']), end='')
    print()

while True:
    print('--' * 30)
    print('Os jogadores são identificados por sua ordem de cadastro.')
    OrdinalNumberInput = int(input('Mostrar dados de qual jogador? '))

    for PositionPlayer, InformationPlayer in enumerate(ListPlayerFull):
        if PositionPlayer == OrdinalNumberInput:
            for OrdinalNumber, NameAndGoals in enumerate(InformationPlayer):
                print('--' * 30)
                print('LEVANTAMENTO DO JOGADOR: {}'.format(NameAndGoals['Nome']))
                for Match, GoalsPerMatch in enumerate(NameAndGoals['Gols']):
                    print('Na partida {}, fez {} gol(s).'.format(Match + 1, GoalsPerMatch))
                    break
        elif OrdinalNumberInput >= len(ListPlayerFull):
            print('Não existe jogador com este número.')
            break

    StopConditionTwo = str(input('Deseja continuar digitando? \nSim ou Não: ')).strip().upper()[0:3]
    while StopConditionTwo not in 'SIMNÃO':
        StopConditionTwo = str(input('Deseja continuar digitando? \nSim ou Não: ')).strip().upper()[0:3]
    if StopConditionTwo == 'NÃO':
        break
