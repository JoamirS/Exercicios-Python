# print string upper

class A:
    attribute_a = 'valor a'

    def method(self):
        print('A')


class B(A):
    attribute_b = 'valor b'

    def method(self):
        print('B')


class C(B):
    attribute_c = 'valor c'

    def method(self):
        super(C, self).method()
        print('C')


class_c = C()
print(class_c.attribute_a)
print(class_c.attribute_b)
print(class_c.attribute_c)
class_c.method()
