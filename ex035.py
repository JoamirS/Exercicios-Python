#   Faça um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#   Declarando as váriaveis que servirão de input
print('Infome as três retas!')
distance1 = int(input('Digite o primeiro valor: '))
distance2 = int(input('Digite o segundo valor: '))
distance3 = int(input('Digite o terceiro valor: '))

if distance1 < distance2 + distance3 and distance2 < distance1 + distance3 and distance3 < distance1 + distance2:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima não podem formar um triângulo')