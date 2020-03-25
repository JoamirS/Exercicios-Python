"""
    Crie um pacote chamado utilities que tenha dois módulos internos chamados moeda e data. Transfira todas funções
    utilizadas nos desafios 107,108 e 109 para o primeiro pacote e mantenha tudo funcionando.
"""
from utilities import moeda
from utilities import dado

inputPriceUser = dado.readMoney('Digite o preço: R$ ')
inputIncreaseUser = int(input('Digite a porcentagem de aumento: '))
inputDecreaseUser = int(input('Digite a porcentagem de redução: '))
moeda.resume(inputPriceUser, inputIncreaseUser, inputDecreaseUser)
