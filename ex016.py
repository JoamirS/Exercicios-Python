#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua poção inteira.
# EX: Digite um número: 6.127. o número 6.127 tem a parte inteira 6
# from math import trunc
# num = float(input('Digite um valor: '))
# print('O valor digitando foi {} e a sua porção inteira é {}'.format(num, trunc(num)))#Esse comando 'trunc' corta o número e retorna a parte inteira

# ----------------- Outra forma de fazer o mesmo código ----------------------------------
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
