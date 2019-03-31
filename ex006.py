#Escreva um programa que leia um número inteiro e calcule o dobro, o triplo e raiz quadrada
n = int(input('Digite um número inteiro: '))
d = n * 2
t = n * 3
r = float(n ** (1/2))
print('O dobro de {} é: {}.'.format(n, d), '\nO triplo de {} é: {}.'.format(n, t), '\nA raiz quadrada de {} é: {:.2f}.'.format(n, r))
