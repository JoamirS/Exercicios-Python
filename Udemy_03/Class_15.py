"""
Exercise with classes
1 - Create a class Car (Name)
2 - Create a class Engine (Name)
3 - Create a class Manufacturer (Name)
4 - Make a connection between Car and Engine
PS: One Engine can be used in many cars
5 - Make a connection between Car and Manufacturer
PS: A Manufacturer can manufacture many cars
Show the name of the car, engine and manufacturer
"""


class Car:
    _manufacturer = None
    _engine = None

    def __init__(self, name):
        self.name = name

    @property
    def get_engine(self):
        return self._engine

    @get_engine.setter
    def get_engine(self, value):
        self._engine = value

    @property
    def get_manufacturer(self):
        return self._manufacturer

    @get_manufacturer.setter
    def get_manufacturer(self, value):
        self._manufacturer = value


class Engine:
    def __init__(self, name):
        self.name = name


class Manufacturer:
    def __init__(self, name):
        self.name = name


volvo_car = Car('SUV EX30')

engine_electric = Engine('Electric permanent magnet')
volvo_car.get_engine = engine_electric.name
print(volvo_car.get_engine)

manufacturer_factory = Manufacturer('VOLVO')
volvo_car.get_manufacturer = manufacturer_factory.name
print(volvo_car.get_manufacturer)

print(volvo_car.__dict__)
