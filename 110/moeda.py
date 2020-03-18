def moeda(number=0, moeda='R$'):
    return f'{moeda}{number:.2f}'.replace('.', ',')


def increase(number, formatted=False):
    increaseTwenty = (number * 0.20) + number
    return increaseTwenty if formatted is False else moeda(increaseTwenty)


def decrease(number, formatted=False):
    decreaseTen = number - (number * 0.10)
    return decreaseTen if formatted is False else moeda(decreaseTen)


def double(number, formatted=False):
    doubleValue = number * 2
    return doubleValue if formatted is False else moeda(doubleValue)


def half(number, formatted=False):
    halfNumber = number / 2
    return halfNumber if formatted is False else moeda(halfNumber)
