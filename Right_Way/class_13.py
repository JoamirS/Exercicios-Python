"""
Create a system to be used for an inventory control team in a distribution center.
Imagine at the end of the day, the team count how many units of products there are in the inventory.
If we had less stock than allowed for that product category, the team must be warned to do a new order for this product.
Each category of a product has a different minimum stock, according to the rules:
    foods > minimum stock: 50
    drink > minimum stock: 75
    cleaning products > minimum stock: 30

For that, we will create a program to ask three inputs of the user: product name, category and current amount of stock.

If the product is over down minimum inventory of his category, the program must be print the message:
    - To request {product} to a purchasing team, we have only {amount} in inventory.
"""
from class_13B import validate_input
import sys

product_name = input('Qual é o nome do produto? ')
print('Escolha uma das três opções: Comida 1 | Bebida 2 | Produtos de limpeza 3')
category_product = int(input('Qual é a categoria do produto? '))

input_user_validation_category_product = validate_input(category_product)

if not input_user_validation_category_product:
    print('Você não digitou um produto válido')
    sys.exit()

current_amount_of_stock = int(input('Qual é a quantidade atual do produto? '))

MINIMUM_VALUE_TO_FOOD = 50
MINIMUM_VALUE_TO_DRINK = 75
MINIMUM_VALUE_TO_CLEANING_PRODUCTS = 30

list_minimum_stock_of_category_product = list()
list_minimum_stock_of_category_product.append(MINIMUM_VALUE_TO_CLEANING_PRODUCTS)
list_minimum_stock_of_category_product.append(MINIMUM_VALUE_TO_DRINK)
list_minimum_stock_of_category_product.append(MINIMUM_VALUE_TO_FOOD)


# Usar estrutura if e elif
def validate_stock(amount_in_stock):
    if amount_in_stock < list_minimum_stock_of_category_product[0]:
        print(f'Passe o {product_name} para o setor de compras, está abaixo do estoque mínimo.')
    elif amount_in_stock < list_minimum_stock_of_category_product[1]:
        print(f'Passe o {product_name} para o setor de compras, está abaixo do estoque mínimo.')
    elif amount_in_stock < list_minimum_stock_of_category_product[2]:
        print(f'Passe o {product_name} para o setor de compras, está abaixo do estoque mínimo.')


validate_stock(current_amount_of_stock)
