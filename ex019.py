#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o
#nome do escolhido
#   Importando a biblioteca randon e importando o método choice
from random import choice
#   Declarando a primeira variavél
a1 = str(input('Primeiro Aluno: '))
#   Declarando a segunda variavél
a2 = str(input('Segundo Aluno: '))
#   Declarando a terceira variavél
a3 = str(input('Terceiro Aluno: '))
#   Declarando a quarta variavél
a4 = str(input('Quarto Aluno: '))
#   Criando uma lista para a escolha
lista = [a1, a2, a3, a4]
#Declarando uma variável que irá receber o valor da lista pelo método choice
escolhido = choice(lista)
#   Printando na tela o número escolhido
print('O aluno escolhido foi {}'.format(escolhido))

