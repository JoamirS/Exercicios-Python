"""
Higher Order Functions
Funções de primeira classe

Os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.
"""


def apply_operation(operation, a, b):
    return operation(a, b)


def soma(a, b):
    return a + b


result = apply_operation(soma, 3, 4)
print(result)  # output: 7
