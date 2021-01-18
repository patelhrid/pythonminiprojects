num = int(input("Enter an integer: "))
a = range(1, num)
list = []

for element in a:
    if (num%element) == 0:
        list.append(element)
print(list)