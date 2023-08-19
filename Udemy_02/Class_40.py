# filter is a functional filter
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


products = [
    {'Name': 'Product 5', 'Price': 10.00},
    {'Name': 'Product 1', 'Price': 22.32},
    {'Name': 'Product 3', 'Price': 10.11},
    {'Name': 'Product 2', 'Price': 105.87},
    {'Name': 'Product 4', 'Price': 69.90}
]

# new_products = [product for product in products if product['Price'] > 10]
new_product = filter(lambda product: product['Price'] > 10, products)

print_iter(products)
print_iter(new_product)
