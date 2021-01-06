number = int(input("Enter a number: "))
remainder = number % 2
multiple = number % 4

if remainder == 0 and multiple==0:
    print("The number you entered, " + str(number) + ", is even and a multiple of 4.")
elif remainder != 0 and multiple==0:
    print("The number you entered, " + str(number) + ", is odd but a multiple of 4.")
elif remainder == 0 and multiple != 0:
    print("The number you entered, " + str(number) + ", is even but not a multiple of 4.")
else:
    print("The number you entered, " + str(number) + ", is odd and not a multiple of 4.")