#Escreva um programa que converta graus Celsius °C em Fahrenheit °F
# Formula para a construção do programa (0 °C × 9/5) + 32 = 32 °F)
c = float(input('Informe a temperatura em °C: '))
f = (c * 9/5) + 32
print('A temperatura de {:.1f} °C corresponde a {:.1f} °F  '.format(c, f))

