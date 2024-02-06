import os
from dotenv import load_dotenv

load_dotenv()
# print(os.getenv('SENHA'))

print(os.environ)
print(os.getenv('APPDATA'))
