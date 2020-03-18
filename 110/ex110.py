"""
    Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
    retornando por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
import moeda
inputUser = int(input('Digite o preço: R$ '))
print(f'O valor do aumento de 20% de {moeda.moeda(inputUser)} é {moeda.increase(inputUser, True)}')
print(f'O valor do desconto de 10% de {moeda.moeda(inputUser)} é {moeda.decrease(inputUser, True)}')
print(f'O valor do dobro de {moeda.moeda(inputUser)} é {moeda.double(inputUser, True)}')
print(f'O valor da metade de {moeda.moeda(inputUser)} é {moeda.half(inputUser, True)}')
