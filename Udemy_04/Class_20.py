"""
string Template for replace text in variable
Methods:
    substitute: replace but generate errors if missing keys
    safe_substitute: replace without generate errors
    You can change the deliminator and another things creating a subclass of template
"""
import json
import locale
import string
from datetime import datetime
from pathlib import Path

locale.setlocale(locale.LC_ALL, '')

FILE_PATH = Path(__file__).parent / 'class_20.txt'


def convert_to_brl(number: float | int) -> str:
    brl = locale.currency(val=number, symbol=True, grouping=True)
    return brl


date = datetime(2022, 12, 28)
data = dict(name='Joamir', value=convert_to_brl(1_234_456),
            date=date.strftime('%d/%m/%Y'), company='J.M.',
            phone='+55 (11) 7890-5432')

print(json.dumps(data, indent=2))

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    text = file.read()
    template = string.Template(text)
    print(template.substitute(data))
