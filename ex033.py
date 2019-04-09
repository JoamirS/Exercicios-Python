#   Faça um programa que leia três números e mostre qual é o maior e qual é o menor

#   Declarando as variáveis a serem recebidas pelo usuário
one = int(input('Digite o primeiro número: '))
two = int(input('Digite o segundo número: '))
three = int(input('Digite o terceiro número: '))
#   Primeira condição a ser percorrida pelo programa
small = one
if two < one and two < three:
    small = two
if three < one and three < two:
    small = three
#   Segunda condição a ser percorrida pelo programa
tall = one
if two > one and two > three:
    tall = two
if three > one and three > two:
    tall = three
print('O maior número é {}'.format(tall))
print('o menor número é {}'.format(small))
