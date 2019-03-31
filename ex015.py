#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 Km rodado.
Km = float(input('Quantos quilômetros foram percorridos pelo carro?\nQuilômetros percorridos: '))
dias = float(input('Qual foi a quatidade de dias que ele foi alugado?\nDias alugados: '))
pago = (dias * 60) + (Km * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(pago))

