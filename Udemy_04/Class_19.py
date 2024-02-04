# secrets generate random safe numbers

import secrets
import string
from secrets import SystemRandom as Sr

random = secrets.SystemRandom()

print(secrets.randbelow(100))
print(secrets.choice(['10', '11', '12']))

print(Sr().choices(string.ascii_letters + string.digits + string.punctuation, k=12))
