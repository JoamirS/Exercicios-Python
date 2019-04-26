'''
    A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de acordo com a idade:
    - Até 9 anos: MIRIM | - Até14 anos: INFANTIL | - Até 19 anos: JUNIOR | - Até 25 anos: Sênior | - Acima: Master
'''
#Importando o módulo
from datetime import date
#Declarando as varíaveis
actually = date.today().year
birth = int(input('Digite seu ano de nascimento: '))
age = actually - birth
if age <= 9:
    print('Sua categoria é MIRIM!')
elif age <= 14:
    print('Sua categoria é INFATIL!')
elif age <= 19:
    print('Sua categoria é JUNIOR!')
elif age <= 25:
    print('Sua categoria é SÊNIOR!')
elif age > 25:
    print('Sua categoria é MASTER!')