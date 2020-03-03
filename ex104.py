"""
    Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
    quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
    sido informado corretamente.
"""


def ficha(Name='Desconhecido', Goals=0):
    print(f'O jogador {Name} marcou {Goals} gol(s) neste campeonato.')


namePlayer = str(input('Qual é o nome do jogador? '))
goalsScored = str(input('Quantos gols ele marcou? '))

if goalsScored.isnumeric():
    goalsScored = int(goalsScored)
else:
    goalsScored = 0

if namePlayer.strip() == '':
    ficha(Goals=goalsScored)
else:
    ficha(namePlayer, goalsScored)
