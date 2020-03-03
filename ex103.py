"""
    Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
    e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de
    cálculo do fatorial.
"""
listRegressiveCount = list()


def fatorial(fatorialInput, Show=False):
    fixedValueFatorial = fatorialInput
    resultFatorial = 1

    while fatorialInput >= 1:
        resultFatorial *= fatorialInput
        listRegressiveCount.append(fatorialInput)
        fatorialInput -= 1

    if Show == True:
        print(f'O cálculo do fatorial de {fixedValueFatorial} é ', end='')

        for Numbers in listRegressiveCount:
            print(Numbers, end='')
            if Numbers == 1:
                print(f': {resultFatorial}')
                break
            print(' * ', end='')

    else:
        print(f'O fatorial de {fixedValueFatorial} é:\n {resultFatorial}')


inputFatorialNumber = int(input('Qual o número deseja saber o fatorial? '))
showcalculed = str(input('Deseja mostrar o cálculo? Sim ou Não '))[0].upper()
if showcalculed == 'S':
    fatorial(inputFatorialNumber, True)
else:
    fatorial(inputFatorialNumber)
