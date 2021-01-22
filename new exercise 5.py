import random

a = range(1, random.randint(1,30))
b = range(10, random.randint(10,40))
list = []

for element in a:
    for element2 in b:
        if element2 == element:
            list.append(element)

print(list)
