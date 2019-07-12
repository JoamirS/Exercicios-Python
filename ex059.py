'''
    Crie um programa que leia dois valores e mostre um menu na tela:
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa
        Seu porgrama deverá realizar a operação solicitada em cada caso.
'''

# Declarando as variáveis
NumberOne = int(input('Digite o primeiro número: '))
NumberTwo = int(input('Digite o segundo número: '))
NumberFunction = 0

while NumberFunction != 5:
    # Mostrando as opções para o usuário
    print('Tecle [1] para somar os dois números')
    print('Tecle [2] para multiplicar os dois números')
    print('Tecle [3] para descobrir qual o maior número')
    print('Tecle [4] para digitar dois mais números')
    print('Tecle [5] para sair do programa')
    NumberFunction = int(input('Faça a opção desejada'))

    # Soma
    if NumberFunction == 1:
        SumNumber = NumberOne + NumberTwo
        print('A soma dos dois números é {}'.format(SumNumber))
    # Multiplicação
    if NumberFunction == 2:
        MultiplyNumber = NumberOne * NumberTwo
        print('Os dois números multiplicados são {}'.format(MultiplyNumber))
    # Maior
    if NumberFunction == 3:
        if NumberOne > NumberTwo:
            print('O primeiro número é maior que o segundo')
        else:
            print('O segundo número é maior que o primeiro')

    # Novos números
    if NumberFunction == 4:
        print('Infome os números novamente:')
        NumberOne = int(input('Informe o primeiro número novamente'))
        NumberTwo = int(input('Informe o segundo número novamente'))
    # Sair do programa
    if NumberFunction == 5:
        print('Fim do programa.')








