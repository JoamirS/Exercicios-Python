number = input('Digite um número que será dobrado: ')


try: # tentar executar o código
    number_float = float(number)
    print('FLOAT:', number_float)
    print(f'O dobro de {number} é o {number_float * 2:.2f}')
except:
    print('Isso não é um número')

# deixando o número sem casas decimais
print(f'O dobro de {number} é {number_float * 2:.0f}')
