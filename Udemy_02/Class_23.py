"""
Try, except, else and finally
"""

try:
    print('Abrir arquivo')
    exception_error = 8 / 0
except ZeroDivisionError:
    print('Dividiu por zero')
else:
    print('Não deu erro')
finally:
    print('Fechar arquivo')
