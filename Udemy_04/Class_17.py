"""
csv.reader and csv.DictReader
csv.reader read the CSV in list format
csv DictReader read CSV in dictionary format
"""

import csv
from pathlib import Path

path_csv = Path(__file__).parent / 'aula_17.csv'

list_clients = [
    {'Name': 'Luiz Otávio', 'Address': 'Av 1, 22'},
    {'Name': 'João Silva', 'Address': 'R.2, "1"'},
    {'Name': 'Maria Sol', 'Address': 'Av B, 3A'}
]

with open(path_csv, 'w') as file:
    name_columns = list_clients[0].keys()
    writer = csv.DictWriter(file, fieldnames=name_columns)

    writer.writeheader()

    for client in list_clients:
        print(client)
        writer.writerow(client)

# with open(path_csv, 'w') as file:
#     name_columns = list_clients[0].keys()
#     writer = csv.writer(file)
#
#     writer.writerow(name_columns)
#
#     for client in list_clients:
#         writer.writerow(client.values())
