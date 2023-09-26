"""
Python 3 use C3 superclass linearization to generate mro.
To know the order of method calls.
Use the class method Class.mro() or the attribute __mro__ (Dunder - Double Underscore)
"""


class A:
    ...

    def who_am_i(self):
        print('A')


class B (A):
    ...

    def who_am_i(self):
        print('B')


class C (A):
    ...

    def who_am_i(self):
        print('C')


class D (B, C):
    ...

    # def who_am_i(self):
    #     print('D')


class_d = D()
class_d.who_am_i()
print(D.__mro__)