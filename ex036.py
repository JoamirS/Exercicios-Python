'''

    Faça um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
    o salário do comprador e em quantos anos ele vai pagar.

    Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

'''

#   Declarando as varáveis
house = float(input('Qual o valor da casa? R$ '))
sal = float(input('Qual é o valor do seu salário? R$ '))
year = int(input('Em quantos anos você deseja pagar? '))
#   Calculando a prestação
installment = house / (year * 12)
print('Para pagar uma casa de R${:.2f} em {} anos\na prestação será de {:.2f}'.format(house, year, installment))
#   Condições para conceder o empréstimo
if installment < ((sal * 30) / 100):
    print('Empréstimo bancário concedido com sucesso para sua casa!')
    print('Realize seu sonho!')
else:
    print('Empréstimo bancário negado. Sua renda não é passivel de pagamento')
    print('Sua renda precisa ser maior para que possa realizar este sonho')
