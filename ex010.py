#Faça um programa que converta R$ em dolar US$
#   Valores baseados no dia da construção do código
real = float(input('Quanto dinhero você tem na carteira? R$ '))
dolar = real / 3.72
euro = real / 4.22
libra = real / 4.86
Guarani = real / 0.00061
print('Com R$ {} você pode comprar US$ {:.2f} Dólares'.format(real, dolar))
print('Com R$ {} você pode comprar € {:.2f} Euros'.format(real, euro))
print('Com R$ {} você pode comprar ₲ {:.2f} Guaranis'.format(real, Guarani))
print('Com R$ {} você pode comprar £ {:.2f} Libras Esterlinas\n'.format(real, libra))


