"""
    Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
    conteúdo da estrutura na tela
"""
ListGradeStudent = []
DictionaryNameAndAverage = dict()

DictionaryNameAndAverage['Nome'] = str(input('Digite o nome do aluno: '))
DictionaryNameAndAverage['Média'] = float(input('Digite a média {}: '.format(DictionaryNameAndAverage['Nome'])))

ListGradeStudent.append(DictionaryNameAndAverage.copy())

for Value in ListGradeStudent:
    for Key, Data in Value.items():
        print('{} é igual a {}'.format(Key, Data))

if ListGradeStudent[0]['Média'] < 7:
    print('Você está reprovado!')
else:
    print('Você está aprovado!')
