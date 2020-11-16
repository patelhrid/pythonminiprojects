name = input("What is your name? ")
age = float(input("What is your age? "))

if age == "1":
    print("Hello " + name + ", you are " + str(age) + " year old.")
else:
    print("Hello " + name + ", you are " + str(age) + " years old.")

time_to_hundred = 100 - age

print("You will be 100 in " + str(time_to_hundred) + " years.")
