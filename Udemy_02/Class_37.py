"""
Count is a counter without end
"""
from itertools import count

count_1 = count(10)  # start with 10, for sample
print(next(count_1))
print(next(count_1))

for iterator in count_1:
    if iterator > 100:
        break
    print(iterator)
