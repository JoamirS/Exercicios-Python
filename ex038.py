'''
    Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    O primeiro valor é maior | O segundo valor é maior | Não existe valor, os dois são iguais
'''

numb1 = int(input('Digite o primeiro valor: '))
numb2 = int(input('Digite o segundo valor: '))
if numb1 > numb2:
    print('O primeiro valor é maior')
elif numb2 > numb1:
    print('O segundo valor é maior')
elif numb1 == numb2:
    print('Não existe valor maior, os dois são iguais')
