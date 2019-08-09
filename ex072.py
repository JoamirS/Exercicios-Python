'''
    Crie um programa que tenha ua tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
    Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

NameNumbersFromZeroToTwenty = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                               'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
                               'eighteen', 'nineteen', 'twenty')

while True:
    NumberInputUser = int(input('Digite um número entre 0 a 20: '))

    while NumberInputUser < 0 or NumberInputUser > 20:
        NumberInputUser = int(input('Digite um número de 0 a 20: '))

    print('O número que você digitou foi {}'.format(NameNumbersFromZeroToTwenty[NumberInputUser]))

    StopOrContinueCondition = str(input('Deseja continuar? Sim ou Não ')).strip().upper()[0]
    if StopOrContinueCondition == 'N':
        break
