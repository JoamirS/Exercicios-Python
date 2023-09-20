"""
Relationship between classes: Aggregation.
Aggregation is a way more specialized of association between two or more objects.
Each object will have your life circle independent.
In General, is a relationship one to many, where an object has one or many objects.
The objects can live separately, but it may a relationship where one object needs another to perform a certain task.
(There are controversies about its definition)
"""


class ShoppingCart:
    def __init__(self):
        self._products_list = []

    def total(self):
        return sum([product.price for product in self._products_list])

    def list_products(self):
        for product in self._products_list:
            print(product.name, product.price)

    def insert_product(self, *products):
        self._products_list.extend(products)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


shopping_cart_01 = ShoppingCart()
product_01, product_02 = Product('Caneta', 1.20), Product('Camiseta', 20)
shopping_cart_01.insert_product(product_01, product_02)
shopping_cart_01.list_products()
print(shopping_cart_01.total())
