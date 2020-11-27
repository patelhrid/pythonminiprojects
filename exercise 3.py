a = [1, 3 , 2, 5, 6, 15, 3, 11, 5.1, 4.9]
b = [1, 3, 2, 3, 4.9]
print(b)

num = float(input("Pick a number: "))

for element in a:
    if element < num:
        print(element)