word = input("Enter a word: ")
list = []
list2 = []

for c in word:
    list.append(c)
    list2.append(c)

list2.reverse()

for element in list:
    for element2 in list2:
        if element == element2:
            

print(list)
print(list2)
