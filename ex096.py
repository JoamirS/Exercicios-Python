""" Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e
    comprimento) e mostre a área do terreno
"""


def area(width, length):
    retanglearea = width * length
    print('A área do terreno de {:.1f} M x {:.1f} M é de {:.1f} M²'.format(width, length, retanglearea))


print('Controle de terrenos')
print('-' * 40)
widthInput = float(input('Qual é a largura? '))
lengthInput = float(input('Qual é o comprimento? '))

area(width=widthInput, length=lengthInput)


