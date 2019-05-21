'''
    Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
# Declarando as varíaveis
biggerWeight = 0
smallerWeight = 0
# Criando o laço
for weight in range(1, 6):
    weightEntered = float(input('Digite o {}º peso: '.format(weight)))
    if weight == 1:
        biggerWeight = weightEntered
        smallerWeight = weightEntered
    else:
        if weightEntered > biggerWeight:
            biggerWeight = weightEntered
        if weightEntered < smallerWeight:
            smallerWeight = weightEntered
print('O maior peso lido foi de {} KG'.format(biggerWeight))
print('O menor peso lido foi de {} KG'.format(smallerWeight))

