"""
    Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só
    que fazendo a validação para aceitar apenas um valor numérico.
"""


def readInt(numberEntered):
    ok = False
    numericValue = 0
    while True:
        numberInVerification = str(input(numberEntered))
        if numberInVerification.isnumeric():
            numericValue = int(numberInVerification)
            ok = True
        else:
            print('Digite um número inteiro válido.')
        if ok:
            break
    return numericValue


numberVerified = readInt('Digite um valor numérico: ')
print(f'O número que você digitou é o {numberVerified}')
