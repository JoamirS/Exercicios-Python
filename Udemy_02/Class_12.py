"""
Introduction lambda function
"""

list_lambda = [
    {'Nome': 'Daniel', 'Sobrenome': 'Silva'},
    {'Nome': 'Eduardo', 'Sobrenome': 'Moreira'},
    {'Nome': 'Aline', 'Sobrenome': 'Souza'}
]

list_lambda.sort(key=lambda item: item['Nome'])

for item_list in list_lambda:
    print(item_list)
