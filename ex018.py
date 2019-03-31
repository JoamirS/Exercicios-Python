#   Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo.

#   Importando a biblioteca matemática e impostando radianos, seno, cosseno, tan
from math import radians, sin, cos, tan
#   Recebendo o valor do ângulo do usuário
ângulo = float(input('Digite o ângulo que você deseja: '))
#   Calculando o seno do angulo em radianos, utilizando a biblioteca
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
#   Calculando o cosseno do angulo em radianos, utilizando a biblioteca
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
#   Calculando a tangente do angulo em radianos, utilizando a biblioteca
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))
