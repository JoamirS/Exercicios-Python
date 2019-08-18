'''
    Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
    cada palavra, quais são as suas vogais.
'''

TupleCursoEmVideo = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
                     'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for ElementsTupleName in TupleCursoEmVideo:
    print('\nNa palavra {} temos as vogais '.format(ElementsTupleName), end='')
    for VowelsWorld in ElementsTupleName:
        if VowelsWorld in 'AEIOU':
            print(VowelsWorld, end=' ')
