"""
Create a program of query drink, given any code, identify whether the drink is alcoholic or not.
"""

coca_cola_code = 'BEB1300543'
pepsi_code = 'BEB1300545'
wine_primitive_lucarelli = 'BAC1546001'
vodka_smirnoff = 'BAC17675002'

list_drinks = list()
list_drinks_alcoholic = []

list_drinks.append(coca_cola_code)
list_drinks.append(pepsi_code)
list_drinks.append(wine_primitive_lucarelli)
list_drinks.append(vodka_smirnoff)

for drink in list_drinks:
    if 'BAC' in drink:
        print(f'A bebida {drink} é alcólica.')
    else:
        print(f'A bebida {drink} não é alcólica.')
