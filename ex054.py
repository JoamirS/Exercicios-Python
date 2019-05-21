'''
    Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
    atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
currentYear = date.today().year
numberPersonAdulthood = 0
NumberPersonNoAdulthood = 0
for birth in range(1, 8):
    yearOfBirth = int(input('Digite o {}º ano de nascimento: '.format(birth)))
    age = currentYear - yearOfBirth
    if age >= 18:
        numberPersonAdulthood += 1
    else:
        NumberPersonNoAdulthood += 1
print('O número de pessoas na maioridade são {} pessoas'.format(numberPersonAdulthood))
print('O númeoro de pessoas que ainda não é maior de idade, são {} pessoas.'.format(NumberPersonNoAdulthood))

