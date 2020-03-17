"""
    Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
    Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
import moeda
inputUser = int(input('Digite o preço: R$ '))
print(f'O valor do aumento de 20% de {inputUser} é {moeda.increase(inputUser)}')
print(f'O valor do desconto de 10% de {inputUser} é {moeda.decrease(inputUser)}')
print(f'O valor do dobro de {inputUser} é {moeda.double(inputUser)}')
print(f'O valor da metade de {inputUser} é {moeda.half(inputUser)}')
