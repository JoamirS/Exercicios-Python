'''
    Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
    perguntar se o usuário quer ou não continuar. No final, mostre:
    A) Quantas pessoas tem mais de 18 anos. | B) Quantos homens foram cadastrados | C) Quantas mulheres tem menos de
    20 anos.
'''

NumberOfWomenUnderTwenty = 0
NumberPeopleAdult = 0
NumberMenRegister = 0
InitialInputCondition = 'S'

while True:
    print('|', '-' * 25, '|')
    print('     Cadastre uma pessoa')
    print('|', '-' * 25, '|')

    AgeOfPerson = int(input('Qual é a sua idade: '))
    SexOfPerson = str(input('Qual é o seu sexo? ')).upper()[0]
    while SexOfPerson not in 'MF':
        SexOfPerson = str(input('Qual é o seu sexo? '))

    if AgeOfPerson >= 18:
        NumberPeopleAdult += 1

    if SexOfPerson == 'M':
        NumberMenRegister += 1

    if AgeOfPerson < 20 and SexOfPerson == 'F':
        NumberOfWomenUnderTwenty += 1

    InitialInputCondition = str(input('Deseja continuar? Sim ou Não?')).upper()[0]
    if InitialInputCondition == 'N':
        break

print('O número de homens cadastrados é de {}'.format(NumberMenRegister))
print('O número de pessoas adultas cadastradas é de {}'.format(NumberPeopleAdult))
print('O número de mulheres abaixo dos 20 anos de idade é de {}'.format(NumberOfWomenUnderTwenty))