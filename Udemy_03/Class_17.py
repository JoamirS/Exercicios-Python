"""
super() is a super class on in subclass
Main class (Person)
    -> super class, base class, parent class
Child class (Client)
    -> subclass, child class, derived class
"""


class MyString(str):
    def upper(self):
        print('Chamou o Upper')
        return super().upper()


string_test = MyString('Luiz')
print(string_test.upper())
