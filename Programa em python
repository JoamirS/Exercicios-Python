#   Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

#   Importando a biblioteca que irá saber qual é o ano da máquina que faz o input
from datetime import date
print('Quer saber se uma no é Bissexto?')
print('Digite 0 se não souber o seu ano atual.')
#   Declarando a variável que irá ser receber o ano digitado
year = int(input('Digite um ano: '))
#   Fale ao usuário para digite 0, se ele não sabe a data da máquina
if year == 0:
    year = date.today().year
#   Declarando as variáveis que serão usadas como parâmetro
calculationOne = year % 4
calculationTwo = year % 100
#   Fazendo a condição a ser percorrida pelo programa
if calculationOne == 0 and calculationTwo != 0 or year % 400 == 0:
    print('O ano de {} é Bissexto!'.format(year))
else:
    print('O ano de {} não é Bissexto!'.format(year))
