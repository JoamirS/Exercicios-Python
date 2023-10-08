"""
Context Manager with classes
Do you can to implement your own protocols implement the dunder methods that Python will be used.
Duck Typing: It means the data types of variables can change as long as the syntax is compatible.
Python is also a dynamic programming language
"""


class MyContentManager:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('Abrindo o arquivo')
        self._file = open(self.file_path, self.mode, encoding='utf8')
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando o arquivo')
        self._file.close()

        print(exc_type)
        print(exc_val)
        print(exc_tb)

        return True


instance = MyContentManager('class_27', 'w')

with instance as file:
    file.write('Linha 1')
    file.write('Linha 2')
    file.write('Linha 3')
    print('With', file)
