"""
    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
    se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
    acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date

NameInput = str(input('Nome: '))
YearBorn = int(input('Ano de nascimento: '))
WorkCard = int(input('Carteira de trabalho: '))
SexInput = str(input('Seu sexo: ')).upper().strip()[0]

CurrentYear = date.today().year
AgeUser = CurrentYear - YearBorn
RetirementAge = 0

DictionaryDataUser = {'Nome': NameInput, 'Ano de nascimento': YearBorn, 'Carteira de trabalho': WorkCard,
                      'Idade': AgeUser, 'Sexo': SexInput}

print('-' * 36)

if WorkCard == 0:
    for Keys, Values in DictionaryDataUser.items():
        print('O valor de {} é {}'.format(Keys, Values))

else:
    DictionaryDataUser['Ano de contratação'] = int(input('Ano de contratação: '))
    DictionaryDataUser['Salário'] = float(input('Salário: '))

    if DictionaryDataUser['Sexo'] in 'M':
        RetirementAge = (DictionaryDataUser['Ano de contratação'] + 35) - YearBorn

    else:
        RetirementAge = (DictionaryDataUser['Ano de contratação'] + 30) - YearBorn

    DictionaryDataUser['Idade para aposentadoria'] = RetirementAge

    for Keys, Values in DictionaryDataUser.items():
        print('O valor de {} é {}'.format(Keys, Values))
