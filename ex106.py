"""
    Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
    as seguintes informações:
    - Quantidade de notas | - A maior nota | - A menor nota | - A média da turma | - A situação (opcional)
    Adicione também as docstrings
"""
stopCondition = 'S'
listAllGrades = list()
counterTypedValues = 0


def grade(totalInput, Great, Worse, Average):
    dictionaryAllInformations = dict()
    dictionaryAllInformations['Total de notas digitadas'] = totalInput
    dictionaryAllInformations['A maior nota'] = Great
    dictionaryAllInformations['A menor nota'] = Worse
    dictionaryAllInformations['A média das notas'] = Average
    print(dictionaryAllInformations)


while stopCondition != 'N':
    inputGradeUser = float(input('Digite sua nota: '))
    print('Deseja continua digitando: Sim ou Não?')
    stopCondition = str(input('')).upper()[0]

    listAllGrades.append(inputGradeUser)
    counterTypedValues += 1
    if stopCondition == 'N':
        break

highestValueEntered = max(listAllGrades)
lowestValueEntered = min(listAllGrades)
averageGrades = sum(listAllGrades) / len(listAllGrades)

grade(Great=highestValueEntered, Worse=lowestValueEntered, Average=averageGrades, totalInput=counterTypedValues)

