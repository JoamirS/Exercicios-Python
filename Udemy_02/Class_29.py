"""
Increase the prices of the following products by 10%
Create new_products for deep copy

Short the products for descending name
Generate order_products_for_name for deep copy

Short the products crescent price
Create order_products_for_price for deep copy
"""


def increase_ten_percent(*product_description):
    price_select = product_description['Price']
    return price_select


products = [
    {'Name': 'Product 5', 'Price': 10.00},
    {'Name': 'Product 1', 'Price': 22.32},
    {'Name': 'Product 3', 'Price': 10.11},
    {'Name': 'Product 2', 'Price': 105.87},
    {'Name': 'Product 4', 'Price': 69.90}
]

result_product = increase_ten_percent(products)
