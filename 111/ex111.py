"""
    Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
    informações geradas pelas funções que já temos no módulo criado até aqui.
"""
import moeda
inputPriceUser = float(input('Digite o preço: R$ '))
inputIncreaseUser = int(input('Digite a porcentagem de aumento: '))
inputDecreaseUser = int(input('Digite a porcentagem de redução: '))
moeda.resume(inputPriceUser, inputIncreaseUser, inputDecreaseUser)
