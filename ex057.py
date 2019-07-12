'''
    Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
    digitação novamente até ter um valor correto.
'''
# Pedindo o nome do usuário
NamePerson = str(input('Digite seu nome: '))
# Mostrando ao usuário as opções disponíveis
print('M or F')
# Tirando os espaços, colocando tudo em maiusculo, e pegando somente a primeira letra da palavara
MaleOrFemale = str(input('Insira seu sexo: ')).upper().strip()[0]

while MaleOrFemale not in 'FM':
    # Tirando os espaços, colocando tudo em maiusculo, e pegando somente a primeira letra da palavra
    MaleOrFemale = str(input('Sexo digitado incorretamente, digite novamente: ')).upper().strip()[0]
print('Srº {}, seu sexo {} foi cadastrado com sucessso.'.format(NamePerson, MaleOrFemale))

