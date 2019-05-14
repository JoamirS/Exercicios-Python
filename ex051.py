'''
    Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
    dessa progressão.

    Notação Matemática: A fórmula para achar o enésimo termo de uma PA é: an = a1 + (n – 1) . r
    Em que an é o enésimo termo (termo geral); a1 é o primeiro termo; n é o número de termos; r é a razão.
'''
#   Declarando as variáveis
firstNumber = int(input('Digite o primeiro número: '))
ratioArithmeticProgression = int(input('Digite a razão da PA: '))
tenthNumber = firstNumber + (10 - 1) * ratioArithmeticProgression
#   Criando o laço
for c in range(firstNumber, tenthNumber, ratioArithmeticProgression):
    print(c)
