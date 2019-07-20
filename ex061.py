'''
    Refaça o desafio 051, lendo o primeiro termo da razão e a razão de uma PA, mostrando os 10 primeiros termos da
    da progressão usando a estrutura while.

    Notação Matemática: A fórmula para achar o enésimo termo de uma PA é: an = a1 + (n – 1) . r
    Em que an é o enésimo termo (termo geral); a1 é o primeiro termo; n é o número de termos; r é a razão.
'''
# Declarando minhas variáveis
FirstNumber = int(input('Digite o número que começa a razão: '))
RatioArithmeticProgression = int(input('Digite a razão desejada da progressão aritmética: '))
ElementOfArithmeticProgression = FirstNumber
NumberCount = 0
# Criando o laço while
while NumberCount < 10:
    print(ElementOfArithmeticProgression)
    ElementOfArithmeticProgression += RatioArithmeticProgression
    NumberCount += 1
print('Fim do programa.')
