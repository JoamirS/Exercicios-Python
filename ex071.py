'''
    Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunta ao usuário qual será o valor
    a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
    Obeservação: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1
'''

EnterValue = int(input('Digite o valor a ser sacado: '))
countBankNoteFifty = 0
countBankNoteTwenty = 0
countBankNoteTen = 0
countBankNoteOne = 0
remainingAmount = EnterValue

while True:
    if remainingAmount >= 50:
        remainingAmount -= 50
        countBankNoteFifty += 1
    else:
        if remainingAmount >= 20:
            remainingAmount -= 20
            countBankNoteTwenty += 1
        else:
            if remainingAmount >= 10:
                remainingAmount -= 10
                countBankNoteTen += 1
            else:
                if remainingAmount >= 1:
                    remainingAmount -= 1
                    countBankNoteOne += 1
                else:
                    break

if countBankNoteFifty > 0:
    print('Total de {} notas de RS 50,00'.format(countBankNoteFifty))
if countBankNoteTwenty > 0:
    print('Total de {} notas de R$ 20,00'.format(countBankNoteTwenty))
if countBankNoteTen > 0:
    print('Total de {} notas de R$ 10,00'.format(countBankNoteTen))
if countBankNoteOne > 0:
    print('Total de {} notas de R$ 1,00'.format(countBankNoteOne))
