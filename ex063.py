'''
    Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
    sequência de fibonacci.
    Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
'''

# Declarando as minhas variáveis
NumberOfElements = int(input('Digite o número de elementos da sequência que deseja: '))
ElementOne = 0
ElementTwo = 1
NumberCount = 3

#   Mostrando os dois primeiros termos que não será preciso fazer cálculos
print(ElementOne)
print(ElementTwo)

#   Criando meu laço de repetição
while NumberCount < NumberOfElements:
    ElementThree = ElementOne + ElementTwo
    print(ElementThree)
    ElementOne = ElementTwo
    ElementTwo = ElementThree
    NumberCount += 1
print('Fim do programa')
