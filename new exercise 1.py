name = input("What is your name: ")
age = int(input("What is your age: "))
number = int(input("Enter any integer: "))
year = 2020+(100-age)
messages = 1

while messages <= number:
    print("Your name is " + name + ". You will turn 100 in " + str(year) + ".")
    messages += 1