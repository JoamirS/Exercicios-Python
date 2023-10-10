"""
Especial method __call__
callable is something can to be executed with parentheses.
In normal classes, __call__ make an instance of class 'callable'
"""


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, name):
        print(name, 'está chamando:', self.phone)


call_01 = CallMe('5252574689')
call_01('Joamir')