'''
    Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
    No final, mostre:
    a) Qual é o total gasto na compra. | b) Quantos produtos custam mais de R$ 1000. | c) Qual é o produto mais barato.
'''

PurchaseTotal = 0
CounterProductsThatCostOverAThousand = 0
CheapestPriceProduct = 0
CheapestProductName = ' '
RegisteredProductCounter = 0

while True:
    print('-' * 25)
    print('Lojão super Atacadão')
    print('-' * 25)

    NameProduct = str(input('Qual é o nome do produto? '))
    PriceOfProduct = float(input('Qual é o preço do produto? '))

    PurchaseTotal += PriceOfProduct

    RegisteredProductCounter += 1

    if PriceOfProduct > 1000:
        CounterProductsThatCostOverAThousand += 1

    if RegisteredProductCounter == 1 or PriceOfProduct < CheapestPriceProduct:
        CheapestPriceProduct = PriceOfProduct
        CheapestProductName = NameProduct

    ConditionalStatement = str(input('Deseja continuar? Sim ou Não ')).strip().upper()[0]
    while ConditionalStatement not in 'SN':
        ConditionalStatement = str(input('Deseja continuar? Sim ou Não ')).strip().upper()[0]
    if ConditionalStatement == 'N':
        break

print('O total gasto em sua compra é R$ {:.2f}'.format(PurchaseTotal))
print('{} produto(s) custam mais de R$ 1000 '.format(CounterProductsThatCostOverAThousand))
print('O produto com menor preço é a {}, com o preço de {:.2f}'.format(CheapestProductName, CheapestPriceProduct))

