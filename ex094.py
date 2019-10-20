"""
    Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
    e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas cadastradas | B) A média de idade | C) Uma lista com mulheres | D) Uma lista com idade acima da média
"""
StopCondition = 'S'
CounterRegisteredPeople = 0
SumAge = 0
AverageAge = 0
DictionaryInputWoman = dict()
ListAllWoman = list()
DictionaryPeopleUpAverage = dict()
ListAllPeopleUpAverage = list()

while StopCondition != 'N':
    NamePerson = str(input('Cadastrar Nome: '))
    SexPerson = str(input('Cadastrar Sexo: ')).strip().upper()[0]
    while SexPerson not in 'MF':
        print('Erro, digite um valor válido.')
        SexPerson = str(input('Cadastrar Sexo: ')).strip().upper()[0]
    AgePerson = int(input('Cadastrar idade: '))

    CounterRegisteredPeople += 1

    SumAge += AgePerson
    AverageAge = SumAge / CounterRegisteredPeople

    if SexPerson == 'F':
        DictionaryInputWoman['Nome'] = NamePerson
        ListAllWoman.append(DictionaryInputWoman.copy())

    if AgePerson > AverageAge:
        DictionaryPeopleUpAverage['Nome'] = NamePerson
        DictionaryPeopleUpAverage['Sexo'] = SexPerson
        DictionaryPeopleUpAverage['Idade'] = AgePerson
        ListAllPeopleUpAverage.append(DictionaryPeopleUpAverage.copy())

    StopCondition = str(input('Deseja continuar?\nSim ou Não: ')).strip().upper()[0]
    while StopCondition not in 'SN':
        print('Erro! Digitação errada, digite novamente')
        StopCondition = str(input('Deseja continuar?\n Sim ou Não: ')).strip().upper()[0]
    if StopCondition == 'N':
        break

print('A quantidade de pessoas cadastradas é {}'.format(CounterRegisteredPeople))
print('--' * 5)
print('A média de idade das pessoas é {:.2f}'.format(AverageAge))
print('--' * 5)
print('O nome das mulheres cadastradas foi: ', end='')
for ElementsInList in ListAllWoman:
    for Key, Value in ElementsInList.items():
        print(Value, end=' | ')

print('\n', '--' * 5)
print('As pessoas acima da média de idade são:')
for ElementsInList in ListAllPeopleUpAverage:
    for Key, Value in ElementsInList.items():
        CounterUntilThree = 0
        print('{} = {} '.format(Key, Value), end='; ')
