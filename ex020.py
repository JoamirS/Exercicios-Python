# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle
a1 = str(input('Primeiro Aluno: '))
a2 = str(input('Segundo Aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quatro Aluno: '))
lista = [a1, a2, a3, a4]
ordem = shuffle(lista) # Esse método emparalha todos os itens da lista
print('A ordem é {}'.format(lista))
