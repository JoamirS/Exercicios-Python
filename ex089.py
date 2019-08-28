"""
    Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
    um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
ListNameAndGrade = []
ListNameAndGradeTemporary = []

while True:
    InputNameUser = str(input('Digite o nome do aluno(a): '))
    InputFirstGrade = float(input('Digite a primeira nota: '))
    InputSecondGrade = float(input('Digite a segunda nota: '))

    ListNameAndGradeTemporary.append(InputNameUser)
    ListNameAndGradeTemporary.append(InputFirstGrade)
    ListNameAndGradeTemporary.append(InputSecondGrade)

    ListNameAndGrade.append(ListNameAndGradeTemporary[:])
    ListNameAndGradeTemporary.clear()

    StopCondition = str(input('Deseja continuar digitando? \nSim ou Não: ')).strip().upper()[0:3]
    while StopCondition not in 'SIMNÃO':
        StopCondition = str(input('Deseja continuar digitando? \nSim ou Não: ')).strip().upper()[0:3]
    if StopCondition == 'NÃO':
        break

print('Posição |       Nome      | Média')
print('-' * 35)

for PositionStudent, DataStudent in enumerate(ListNameAndGrade):
    AverageGrade = float((DataStudent[1] + DataStudent[2]) / 2)
    print('{:^6}'.format(PositionStudent + 1), end='| ')
    print('{:^10}'.format(DataStudent[0]), end='')
    print('| {}'.format(AverageGrade))
    print('-' * 35)

while True:
    ShowGradeStudent = int(input('Para ver as notas, digite a posição dela(e): '))
    if ShowGradeStudent <= len(ListNameAndGrade) - 1:
        print('A notas de {} são {}'.format(ListNameAndGrade[ShowGradeStudent][0], ListNameAndGrade[ShowGradeStudent][1]))

    StopConditionTwo = str(input('Deseja continuar digitando? \nSim ou Não: ')).strip().upper()[0:3]
    while StopConditionTwo not in 'SIMNÃO':
        StopConditionTwo = str(input('Deseja continuar digitando? \nSim ou Não: ')).strip().upper()[0:3]
    if StopConditionTwo == 'NÃO':
        break

