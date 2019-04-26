'''
    Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
    - Equilátero: Todos os lados iguais
    - Isósceles: Dois lado iguais
    - Escaleno: Todos os lados diferentes

    Relembrando o exercício 035
    Faça um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
#Declarando as variáveis
dist1 = int(input('Digite o primeiro lado: '))
dist2 = int(input('Digite o segundo lado: '))
dist3 = int(input('Digite o terceiro lado: '))
#Criando as condições
if dist1 < dist2 + dist3 and dist2 < dist1 + dist3 and dist3 < dist1 + dist2:
    print('Os lados propostos podem formar um triângulo.')
    if dist1 == dist2 == dist3:
        print('Será formado com esses lados um triângulo EQUILÁTERO!')
    elif (dist1 == dist2 or dist1 == dist3) or (dist2 == dist3 or dist2 == dist1):
        print('Será formado com esses lados um triângulo ISÓSCELES!')
    elif dist1 != dist2 and dist1 != dist3 and dist2 != dist3:
        print('Será formado com esses lados um triângulo ESCALENO!')
else:
    print('Os segmentos acima não podem formar um triângulo.')
