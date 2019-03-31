#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
# cato = float(input('Digite o cpmprimento do cateto oposto: '))
# cata = float(input('Digite o comprimento do cateto adjancente: '))
# hipo = (cato ** 2 + cata ** 2) ** (1/2)
# print('A hipotenusa de {} e de {} é: {:.2f}'.format(cato, cata, hipo))

#--------------- Outra forma de fazer o algoritmo, com importanção
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipo = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hipo))
