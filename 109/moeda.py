def moeda(number=0, moeda='R$'):
    return f'{moeda}{number:.2f}'.replace('.', ',')


def increase(number):
    increaseTwenty = (number * 0.20) + number
    return increaseTwenty


def decrease(number):
    decreaseTen = number - (number * 0.10)
    return decreaseTen


def double(number):
    doubleValue = number * 2
    return doubleValue


def half(number):
    halfNumber = number / 2
    return halfNumber
