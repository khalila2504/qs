import math
print(f'the value of pi is approximately {math.pi:.3f}.')

table = {'sjoerd': 4127, 'jack': 4098, 'dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

animals = 'eels'
print(f'my hovercraft is full of {animals!r}.')