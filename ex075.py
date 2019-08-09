'''
    Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
    A) Quantas vezes apareceu o valor 9 | B) Em que posição foi digitado o valor 3 'pela primeira vez'
    | C) Quais foram os números pares

    OBS: A variável TupleInputsUser é uma variável composta
'''

NumberOne = int(input('Digite o 1º valor: '))
NumberTwo = int(input('Digite o 2º valor: '))
NumberThree = int(input('Digite o 3º valor: '))
NumberFour = int(input('Digite o 4º valor: '))

TupleInputsUser = (NumberOne, NumberTwo, NumberThree, NumberFour)
print('Os números digitados foram {}'.format(TupleInputsUser))

print('O número 9 apareceu {} vezes'.format(TupleInputsUser.count(9)))

if 3 in TupleInputsUser:
    print('O número 3 foi digitado na {}ª posição.'.format(TupleInputsUser.index(3) + 1))
else:
    print('O valor 3 não foi digitado.')

print('Os números pares digitados foram:', end=' ')
for NumbersInTuple in TupleInputsUser:
    if NumbersInTuple % 2 == 0:
        print(NumbersInTuple, end=', ')

