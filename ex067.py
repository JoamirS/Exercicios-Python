'''
    Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
    O programa será cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for
    negativo.
'''

while True:
    InputNumber = int(input('Digite o número da tabuada: '))
    if InputNumber <= 0:
        print('Não existe tabuada de número negativo e de 0')
        break
    for TabuadaNumber in range(1, 11):
        print(f'{TabuadaNumber} * {InputNumber} = {TabuadaNumber * InputNumber}')

print('Fim do programa')
