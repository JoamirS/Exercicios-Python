'''
    Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
    os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
    continuar a digitar valores.
'''
NumberCount = 1
ConditionalParameter = str('SIM')
NumberIntegerTwo = 0

while ConditionalParameter != 'NÃO':
    NumberIntegerOne = int(input('Digite um número inteiro: '))
    MaiorNumber = NumberIntegerOne
    MenorNumber = NumberIntegerTwo

    if NumberIntegerOne < NumberIntegerTwo:
        MenorNumber = NumberIntegerOne
        MaiorNumber = NumberIntegerTwo

    AverageNumber = (NumberIntegerOne + NumberIntegerTwo) / NumberCount
    NumberIntegerTwo = NumberIntegerOne
    NumberCount += 1
    ConditionalParameter = str(input('Deseja continuar digitando um número? \n Tecle [Sim] ou [Não]\n: ')).upper()
print('A média dos números digitados é {}'.format(AverageNumber))
print('O menor número é {} e o maior número é {}'.format(MenorNumber, MaiorNumber))
