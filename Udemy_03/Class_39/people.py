import accounts


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def get_name(self):
        return self._name

    @property
    def get_age(self):
        return self._age

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.get_name}, {self.get_age})'
        return f'{class_name}, {attrs}'


class Client(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.account: accounts.Account | None = None
