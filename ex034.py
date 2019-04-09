#   Escreva um programa que pergunte o salário de um funcioário e calcule o valor do seu aumento.
#   Para salários superiores a 1250.00, calcule um aumento de 10%.
#   para salários inferiores ou iguais, o aumento é de 15%.

#   Declarando a variável que receberá o valor do salário
sal = float(input('Digite o seu salário: RS'))
if sal > 1250.00:
    add = (10 * sal) / 100
    print('O seu salário será aumentado em R${:.2f} reais'.format(add))
if sal <= 1250.00:
    add = (15 * sal) / 100
    print('O seu salário será aumentado em R${:.2f} reais'.format(add))

