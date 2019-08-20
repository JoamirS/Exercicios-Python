"""
    Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
    a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
HeapList = []

InputMathematicalExpression = str(input('Digite a expressão desejada: '))

for Parentheses in InputMathematicalExpression:
    if Parentheses == '(':
        HeapList.append('(')
    elif Parentheses == ')':
        if len(HeapList) > 0:
            HeapList.pop()
        else:
            HeapList.append(')')
            break

PositionFirstOpenParentheses = InputMathematicalExpression.index('(')
PositionFirstCloseParentheses = InputMathematicalExpression.index(')')

if PositionFirstCloseParentheses < PositionFirstOpenParentheses:
    print('Você fechou um parenteses antes de abri-lo')

CounterOpenParenthesis = InputMathematicalExpression.count('(')
CounterCloseParenthesis = InputMathematicalExpression.count(')')

if CounterCloseParenthesis != CounterOpenParenthesis:
    print('O número de parenteses abertos e fechados não é igual.')

if len(HeapList) == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está errada.')