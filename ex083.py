"""
    Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
    a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
InputMathematicalExpression = str(input('Digite a expressão desejada: '))

PositionFirstOpenParentheses = InputMathematicalExpression.index('(')
PositionFirstCloseParentheses = InputMathematicalExpression.index(')')

if PositionFirstCloseParentheses < PositionFirstOpenParentheses:
    print('Sua expressão está errada.')


CounterOpenParenthesis = InputMathematicalExpression.count('(')
CounterCloseParenthesis = InputMathematicalExpression.count(')')

if CounterCloseParenthesis != CounterOpenParenthesis:
    print('Sua expressão está errada.')

else:
    print('Sua expressão está correta.')
