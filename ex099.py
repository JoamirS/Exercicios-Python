""" Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu
    programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
ListWithAllNumbers = list()


def bigger(* numbersvalue):
    if len(numbersvalue) == 1:
        print('O maior e único número passado foi o número {}.'.format(numbersvalue))
    elif len(numbersvalue) > 1:
        SizeList = len(numbersvalue)
        ListWithAllNumbers.append(numbersvalue)
        print('Analizando os números informados:')
        for Allnumberslist in ListWithAllNumbers:
            print(' Os números informados foram {}'.format(Allnumberslist, end=''))
            print(' O maior número passado foi o {}'.format(max(Allnumberslist)))
        print(' Totalizando {} números.'.format(SizeList))
    print('--' * 30)
    ListWithAllNumbers.clear()


bigger(9)
bigger(3, 7)
bigger(4, 8, 10)
bigger(2, 5, 9, 6, 90, 3)
bigger(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
