"""
Take care with amount of parameters.
If you choose to receive data structures like dict,list, tuple and instance of a class is better than immense parameters
"""


class Men:
    def __init__(self, name_men_input):
        self._name_men = name_men_input

    @property
    def name_men(self):
        return self._name_men


def method_with_many_parameters(user_data_input):
    name = user_data_input.name_men
    return name


test_class_02 = Men('Joamir')
test_method_many_parameters = method_with_many_parameters(test_class_02)
print(test_method_many_parameters)
