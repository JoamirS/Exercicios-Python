'''
    Melhore o desafio 061, perguntado para o usuário se ele quer mostrar mais alguns termos. O programa encerra
    quando ele disser que quer mostrar 0 (zero) termos.
'''

# Declarando minhas variáveis
FirstNumber = int(input('Digite o número que começa a razão: '))
RatioArithmeticProgression = int(input('Digite a razão desejada da progressão aritmética: '))
ElementOfArithmeticProgression = FirstNumber
NumberCount = 0
NumberTotal = 0
NumberOfMore = 10
# Criando o laço while
while NumberOfMore != 0:
    NumberTotal = NumberTotal + NumberOfMore
    while NumberCount <= NumberTotal:
        print(ElementOfArithmeticProgression)
        ElementOfArithmeticProgression += RatioArithmeticProgression
        NumberCount += 1
    print('Pausa')
    NumberOfMore = int(input('Quantos termos você quer ver mais desta PA? '))
    print('Digite 0 para sair do programa')
print('O programa foi finalizado com o total de {} elementos da PA.'.format(NumberTotal))
print('Fim do programa!')
