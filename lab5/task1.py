# Write a program that will take a number form user and will display whether the number is even
# or odd. Use if-else statement.

number = int(input("enter a number: "))
if(number%2==0):
    print(f"{number} is positive number")
    print("positive numbers are great!")
else:
    print(f"{number} is a negative number")
    print("negative numbers are scary")

print("Thanks for your time")
