#   Faça um programa que pergunte a distância em Km. calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e
#   e R$ 0,45 para viagens mais longas.

#   Declarando a variável que receberá a distância em Km --|
distance = float(input('Digite a distância em Km: '))
if distance <= 200:
    price = 0.50 * distance
    print('O preço cobrado será de R${:.2f}'.format(price))
else:
    price = 0.45 * distance
    print('O preço cobrado será de R${:.2f}'.format(price))
