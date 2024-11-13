"""
Create a program to print the main KPI of store in the last year. Make using variables.

Values:
    Coca-Cola sales quantity : 150
    Pepsi sales quantity: 130
    Unit price of Coca-Cola : 1,50
    Unit Price of Pepsi : 1,50
    Custo da loja: 2500,00
"""

quantity_pepsi = 130
quantity_coca_cola = 150
unit_price_coca_cola = 1.50
unit_price_pepsi = 1.50

invoicing_store_pepsi = quantity_pepsi * unit_price_pepsi
invoicing_store_coca_cola = quantity_coca_cola * unit_price_coca_cola

print(f'O faturamento com coca-cola foi R$ {invoicing_store_coca_cola} e o faturamento com pepsi foi R$ {invoicing_store_pepsi}')

operating_cost = 2500

print(f'O lucro da loja foi R$ {(invoicing_store_pepsi + invoicing_store_coca_cola) - operating_cost}')

