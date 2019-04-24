'''
    Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    - Se ele ainda vai se alistar ao serviço militar
    - Se é a hora de se alistar
    - Se já passou do tempo do alistamento
    * Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
#Importando o módulo datetime para buscar o ano atual
from datetime import date

#Declarando a variável
year = int(input('Digite seu ano de nascimento: '))
year2 = date.today().year
age = year2 - year
print('Quem nasceu em {} tem {} anos em {}.'.format(year, age, year2))

#Condições a serem retornadas
if age < 18:
    balance = 18 - age
    print('Você ainda se alistará para o serviço militar.\nAinda faltam {} anos para o alistamento'.format(balance))
    year3 = year2 + balance
    print('Seu alistamento será em {}'.format(year3))
elif age == 18:
    print('Você tem que se alistar imediatamente!')
elif age > 18:
    balance = age - 18
    print('Já passou da hora de você se alistar.\nVocê deveria ter se alistado há {} anos.'.format(balance))
    year3 = year2 - balance
    print('Seu alistamento foi em {}'.format(year3))

