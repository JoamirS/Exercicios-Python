'''
   Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do campeonato brasileiro de futebol, depois mostre:
    a) Os 5 primeiros. b) Os últimos 4 colocados. c) times em ordem alfabética d) Em que posição está a chapecoense.
'''

TwentyTeamsFootballBrazil = ('Santos', 'Palmeiras', 'Flamengo', 'Atlético-MG', 'Corinthians', 'São Paulo',
                             'Internacional', 'Athletico-PR', 'Botafogo', 'Bahia', 'Ceará', 'Goiás', 'Grêmio',
                             'Fortaleza', 'Vasco', 'Fluminense', 'Chapecoense', 'Cruzeiro', 'CSA', 'Avaí')

print('Os cinco primeiros times são {} '.format(TwentyTeamsFootballBrazil[0:5]))

print('Os últimos colocados são: {}'.format(TwentyTeamsFootballBrazil[-4:]))

print('Os times em ordem alfabética são : {}'.format(sorted(TwentyTeamsFootballBrazil)))

print('A chapecoense está na posição {}'.format(TwentyTeamsFootballBrazil.index('Chapecoense') + 1))
