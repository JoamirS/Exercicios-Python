'''
    Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço nomal e condição e
    condição de pagamento:
    - À vista dinheiro/cheque: 10% de desconto | - À vista no cartão: 5% de desconto
    - Em até 2x no cartão: preço normal | - 3x ou mais no cartão: 20% de juros
'''
# Declarando as variáveis
priceProduct = float(input('Digite o preço do produto: '))
print('\033[1;34mModelos de pagamento disponíveis:\n[ 1 ] À vista dinheiro/cheque | Desconto 10%\n[ 2 ] À vista no '
      'cartão | Desconto: 5%\n[ 3 ] Em até 2x no cartão | Desconto: 0\n[ 4 ] 3x ou mais no cartão '
      '| Juros 20%\033[0;0m')
paymentMethod = float(input('Qual é a forma de pagamento desejada? '))
#Declarando as condições
if paymentMethod == 1:
    finalProductPrice = priceProduct - ((priceProduct * 10) / 100)
    print('Baseado na sua forma de pagamento, o preço final do produto será R${:.2f}'.format(finalProductPrice))
elif paymentMethod == 2:
    finalProductPrice = priceProduct - ((priceProduct * 5) / 100)
    print('Baseado na sua forma de pagamento, o preço final do produto será R${:.2f}'.format(finalProductPrice))
elif paymentMethod == 3:
    installment = priceProduct / 2
    print('O valor da sua parcela será de {:.2f}'.format(installment))
    finalProductPrice = priceProduct
    print('Baseado na sua forma de pagamento, o preço final do produto será R${:.2f}'.format(finalProductPrice))
elif paymentMethod == 4:
    finalProductPrice = priceProduct + ((priceProduct * 20) / 100)
    totalPlots = int(input('Qual o número de parcelas? '))
    installment = finalProductPrice / totalPlots
    print('Baseado na sua forma de pagamento, sua parcela é {:.2f}'.format(installment))
    print('Baseado na sua forma de pagamento, o preço final do produto será R${:.2f}'.format(finalProductPrice))
else:
    finalProductPrice = priceProduct

    print('Opção inválida de pagamento. Tente novamente!')

