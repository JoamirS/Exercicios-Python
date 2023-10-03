"""
Create Exceptions in Python OO.
To create an exception in Python, you need to inherit some exception language.
The documentation recommends to inherit of Exception.
Create exceptions (Its common to put Error in the end).
Lifting (raise) / Launching (throw) exceptions.
Relaunching exceptions.
Adding notes in Exceptions.
"""


class MyError(Exception):
    ...


class AnotherError(Exception):
    ...


def rise():
    exception = MyError('A', 'B', 'C')
    exception.add_note('Olha a nota 1')
    exception.add_note('Você errou no rise')
    raise exception


try:
    # 1/0
    rise()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception = AnotherError('Vou lançar de novo')
    exception.__notes__ += error.__notes__.copy()
    raise exception from error
