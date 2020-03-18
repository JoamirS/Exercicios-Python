"""
    Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um
    valor monetário formatado.
"""
import moeda
inputUser = int(input('Digite o preço: R$ '))
print(f'O valor do aumento de 20% de {moeda.moeda(inputUser)} é {moeda.moeda(moeda.increase(inputUser))}')
print(f'O valor do desconto de 10% de {moeda.moeda(inputUser)} é {moeda.moeda(moeda.decrease(inputUser))}')
print(f'O valor do dobro de {moeda.moeda(inputUser)} é {moeda.moeda(moeda.double(inputUser))}')
print(f'O valor da metade de {moeda.moeda(inputUser)} é {moeda.moeda(moeda.half(inputUser))}')
