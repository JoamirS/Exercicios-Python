"""
Simple Heritage - Relations between classes
Association - Use; Aggregation - has;
Composition - It is owner of, Heritage - Is one

Main class (Person)
    super class, base class, parent class
Child class (Client)
    subclass, child class, derived class
"""


class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def show_class_name(self):
        print(self.__class__.__name__)
        print(self.name, self.last_name)


class Client(Person):
    ...


class Student(Person):
    ...


client_01 = Client('Joamir', 'Moraes')
student_01 = Student('Luiz', 'Miranda')
client_01.show_class_name()
student_01.show_class_name()
