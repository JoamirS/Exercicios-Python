"""
Save your class in Json
Save the data of your class in Json and load again the instances of class with save data.
Make in separate files
"""
import json


class Computer:
    motherboard = 'Asus'
    power_supply = 'Corsair'

    def __init__(self, brand, year_of_manufacture):
        self.brand = brand
        self.year_of_manufacture = year_of_manufacture


computer_class_dict = Computer.__dict__.items()

computer_class_serializer_attributes = {
    key: value for key, value in computer_class_dict if not key.startswith('__')
}

with open('Class_06_json.json', 'w') as file:
    json.dump(computer_class_serializer_attributes, file, ensure_ascii=False)


data_insert_computer_class = {'brand': 'Dell', 'year_of_manufacture': 2018}
unpacking_variable_computer = Computer(**data_insert_computer_class)

with open('init_object.json', 'w') as object_class:
    json.dump(unpacking_variable_computer.__dict__, object_class)

with open('init_object.json', 'r') as load_json:
    result_instance = json.load(load_json)
    print(type(result_instance))
