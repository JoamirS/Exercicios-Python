'''
    Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    * A média de idade do grupo. | * Qual é o nome do homem mais velho. | * Quantas mulheres têm menos de 20 anos.
'''
#Declarando as variáveis
biggerAgeMan = 0
nameOldMan = ''
totalWomanAge = 0
sumAge = 0
# Criando o laço
for people in range(1, 5):
    print('------- {}º Pessoa -------'.format(people))
    peopleNameEntered = str(input('Nome: '))
    peopleAgeEntered = int(input('Idade: '))
    peopleSexEntered = str(input('Sexo [M/F]: '))
    sumAge += peopleAgeEntered
    if people == 1 and 'Mm':
        biggerAgeMan = peopleAgeEntered
        nameOldMan = peopleNameEntered
    if peopleSexEntered in 'Mm' and peopleAgeEntered > biggerAgeMan:
        biggerAgeMan = peopleAgeEntered
        nameOldMan = peopleNameEntered
    if peopleSexEntered in 'Ff' and peopleAgeEntered < 20:
        totalWomanAge += 1
peopleAgeAverage = sumAge / 4
print('A média de idade do grupo é {}'.format(peopleAgeAverage))
print('A idade do homem mais velho é {} anos, e o seu nome é {}'.format(biggerAgeMan, nameOldMan))
print('O total de mulheres com menos de 20 anos é {}'.format(totalWomanAge))
