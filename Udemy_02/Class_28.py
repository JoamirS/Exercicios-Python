import sys
from Class_27_package.Class_27 import *
from Class_27_package.Class_27 import sum_module

print(__name__)
print(*sys.path, sep='\n')
print(sum_module(1, 2))

