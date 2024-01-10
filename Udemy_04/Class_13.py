"""
csv.reader and csv.DictReader
csv.reader read the CSV in list format
csv.DictReader read the CSV in dict format
"""
import csv
from pathlib import Path

FILE_CSV = Path(__file__).parent / 'Equipamentos sem modelo (Novo).csv'
print(FILE_CSV)

with open(FILE_CSV, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    
    for line in reader:
        print(line)