"""
    Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas funções
    utilizadas nos desafios 107,108 e 109 para o primeiro pacote e mantenha tudo funcionando.
"""
from utilidadesCeV import moeda
inputPriceUser = float(input('Digite o preço: R$ '))
inputIncreaseUser = int(input('Digite a porcentagem de aumento: '))
inputDecreaseUser = int(input('Digite a porcentagem de redução: '))
moeda.resume(inputPriceUser, inputIncreaseUser, inputDecreaseUser)
