'''
    Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço
    for.

    Relebrando o exercício 009: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
'''
chosenTableau = int(input('Digite o número da tabuada que você deseja: '))
print('Será mostrada a tabuada do número escolhido de 1 a 9')
for c in range(1, 11):
    print('{} * {} = {}'.format(chosenTableau, c, chosenTableau * c))
