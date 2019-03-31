#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Qual é o preço do produto? R$ '))
des = preco - (preco * 5/100)
print('O produto que custava R${:.2f}, na promação com desconto de 5% vai custar R${:.2f}'.format(preco, des))