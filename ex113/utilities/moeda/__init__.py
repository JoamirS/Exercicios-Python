def moeda(number=0, moeda='R$'):
    return f'{moeda}{number:.2f}'.replace('.', ',')


def functionIncrease(number, valueOfIncrease, formatted=True):
    percentageValue = valueOfIncrease / 100
    increaseResult = (number * percentageValue) + number
    return increaseResult if formatted is False else moeda(increaseResult)


def functionDecrease(number, valueOfDecrease, formatted=True):
    percentageValue = valueOfDecrease / 100
    decreaseResult = number - (number * percentageValue)
    return decreaseResult if formatted is False else moeda(decreaseResult)


def functionDouble(number, formatted=True):
    doubleValue = number * 2
    return doubleValue if formatted is False else moeda(doubleValue)


def functionHalf(number, formatted=True):
    halfNumber = number / 2
    return halfNumber if formatted is False else moeda(halfNumber)


def resume(ReceivedNumber, ReceivedIncrease, Receiveddecrease):
    print('-' * (4 * len(functionDouble(ReceivedNumber))))
    print('    RESUMO DO VALOR')
    print('-' * (4 * len(functionDouble(ReceivedNumber))))
    print(f'Preço analisado: \tR${ReceivedNumber}')
    print(f'Valor do aumento: \t{functionIncrease(valueOfIncrease=ReceivedIncrease, number=ReceivedNumber)}')
    print(f'Valor do desconto:\t{functionDecrease(valueOfDecrease=Receiveddecrease, number=ReceivedNumber)}')
    print(f'O dobro de {ReceivedNumber}: \t{functionDouble(ReceivedNumber)}')
    print(f'A metade de {ReceivedNumber}: \t{functionHalf(ReceivedNumber)}')
    print('-' * (4 * len(functionDouble(ReceivedNumber))))
