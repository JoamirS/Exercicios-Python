# Mutable parameters problem in python functions

def add_customer(name, list_names=None):
    if list_names is None:
        list_names = []
    list_names.append(name)
    return list_names


list_01 = []
customer_01 = add_customer('Luiz', list_01)
add_customer('Joana', customer_01)
print(customer_01)

customer_02 = add_customer('Helena')
add_customer('Maria', customer_02)
print(customer_02)
