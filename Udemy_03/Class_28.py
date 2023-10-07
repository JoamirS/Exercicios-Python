# Context Manager with function - Creating and using context managers
from contextlib import contextmanager


@contextmanager
def my_open(file_path, mode):
    global file
    try:
        print('Abrindo arquivo')
        file = open(file_path, mode, encoding='utf8')
        yield file
    except TypeError as e:
        print('Você passou mais de um argumento, mensagem da exception:\n', e)
    finally:
        print('Fechando o arquivo')
        file.close()


with my_open('class_28.txt', 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n', 123)
    file.write('Linha 3\n')
    print('With', file)
