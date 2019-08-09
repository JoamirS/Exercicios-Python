'''
    Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. no final
    mostre uma listagem de preços, organizando os dados em forma tabular.
'''

TupleNameCarsAndPrice = ('Onix', 46.590, 'HB20', 44.490, 'Ka', 45.590, 'Prisma', 49.990, 'Kwid', 33.990, 'Gol', 47.020,
                         'Argo', 48.990, 'Renegade', 69.990, 'Polo', 53.590, 'Compass', 116.990)

print('-' * 40)
ListProducts = 'LISTA DE PRODUTOS'
print('{:^40}'.format(ListProducts))
print('-' * 40)

for PositionElementTupleCars in range(0, len(TupleNameCarsAndPrice)):
    if PositionElementTupleCars % 2 == 0:
        print('{:.<30}'.format(TupleNameCarsAndPrice[PositionElementTupleCars]), end='')
    else:
        print('R$ {:>.3f} '.format(TupleNameCarsAndPrice[PositionElementTupleCars]))

print('-' * 40)
