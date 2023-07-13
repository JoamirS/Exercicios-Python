"""
Increase the prices of the following products by 10%
Create new_products for deep copy

Short the products for descending name
Generate order_products_for_name for deep copy

Short the products crescent price
Create order_products_for_price for deep copy
"""
import copy


def increase_ten_percent(product_description, position_list):
    price_select = product_description[position_list]['Price']
    ten_percent = float(price_select * 1.1)
    return f'{ten_percent:.2f}'


products = [
    {'Name': 'Product 5', 'Price': 10.00},
    {'Name': 'Product 1', 'Price': 22.32},
    {'Name': 'Product 3', 'Price': 10.11},
    {'Name': 'Product 2', 'Price': 105.87},
    {'Name': 'Product 4', 'Price': 69.90}
]

position = 0

for product in products:
    product['Price'] = increase_ten_percent(products, position)
    position += 1

new_products = copy.deepcopy(products)

order_products_for_name = sorted(new_products, key=lambda item: item['Name'], reverse=True)

# for item in order_products_for_name:
#     print(item)

order_products_for_name_deep_copy = copy.deepcopy(order_products_for_name)

order_products_for_price = sorted(order_products_for_name_deep_copy, key=lambda price: float(price['Price']))

for item in order_products_for_price:
    print(item)
