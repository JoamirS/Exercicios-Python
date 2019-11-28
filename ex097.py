"""
    Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
    mensagem com tamanho adaptável.
    Ex: escreva('Olá, Mundo!')
    ~~~~~~~~~~~~~~~~~~
    Saída: Olá, mundo!
    ~~~~~~~~~~~~~~~~~~
"""


def write(message):
    sizeMessage = len(message)
    print('~' * sizeMessage)
    print(message)
    print('~' * sizeMessage)


write('Olá, como vai?')
write('Tenha um ótimo dia')
write('Thank you, so much')
