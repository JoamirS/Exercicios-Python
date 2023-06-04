"""
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.
"""


def multiplication(operation, input_number):
    return operation(input_number)


def duplicate(input_duplicate):
    return input_duplicate * 2


def triplicate(input_triplicate):
    return input_triplicate * 3


def quadruplicate(input_quadruplicate):
    return input_quadruplicate * 4


result_01 = multiplication(duplicate, 2)
result_02 = multiplication(triplicate, 3)
result_03 = multiplication(quadruplicate, 6)

print(result_01)
print(result_02)
print(result_03)
