"""
    Faça um mini-sistema que utiliza o interactive help do Python. O usuário vai digitar o comando e o manual vai
    aparecer. Quando o usurário digitar a palavra 'FIM', o programa se encerrará.
"""
from time import sleep
c = ('\033[m',  # 0 - Sem cores
     '\033[0;30;41m',   # 1 - Vermelho
     '\033[0;30;42m',   # 2 - Verde
     '\033[0;30;43m',   # 3 - Amarelo
     '\033[0;30;44m',   # 4 - Azul
     '\033[0;30;45m',   # 5 - Branco
     '\033[7;30m'
     )


def ihelp(document):
    title(f'Acessando o manual do comando \'{document}\'', 4)
    help(document)
    sleep(2)


def title(message, color=0):
    print(c[color], end='')
    size = len(message)
    print('-' * len(message))
    print(message)
    print('-' * len(message))
    print(c[0], end='')
    sleep(1)


comand = ''
while True:
    title('SISTEMA DE AJUDA PyHELP', 2)
    comand = str(input('Função ou biblioteca > '))
    if comand.upper() == 'FIM':
        break
    else:
        ihelp(comand)
title('Até logo', 1)
