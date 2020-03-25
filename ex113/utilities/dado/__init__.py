def readMoney(Message):
    validationCheck = False
    while not validationCheck:
        numberInValidation = str(input(Message)).replace(',', '.')
        if numberInValidation.isalpha() or numberInValidation.strip() == '':
            print(f'Erro. {numberInValidation} é um preço inválido.')
        else:
            validationCheck = True
            return float(numberInValidation)
