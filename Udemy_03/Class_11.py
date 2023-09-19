"""
Encapsulation - (access modifiers: public, protected, private)
Python has not access modifiers
But we can follow conventions:
    without underline: public
    one underline: protected
        cannot be used of class or your subclasses
    two underlines: private
    "name mangling" (disfigurement names) in Python
    Only must be used in class at declared
"""


class Boot:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado'

    def public_method(self):
        return 'Método público'


boot_01 = Boot()
print(boot_01.public)
public_method = boot_01.public_method()
print(boot_01._protected)
print(boot_01.__private)
print(public_method)