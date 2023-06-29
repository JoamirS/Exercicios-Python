"""
Introduction at Generator functions in Python
"""


# def generator(n=0, maximum=10):
#     yield 1  # to pause
#     print('Continuando...')
#     yield 2  # to pause
#     print('Mais uma...')
#     yield 3
#     print('Vou terminar')
#     return 'Acabou'
#
#
# generator_variable = generator(n=0)
# print(next(generator_variable))
# print(next(generator_variable))
# print(next(generator_variable))
#
# for test in generator_variable:
#     print(test)


def generator(number=0, maximum=10):
    while True:
        yield number
        number += 1

        if number > maximum:
            return


generator_variable = generator()
for number in generator_variable:
    print(number)
