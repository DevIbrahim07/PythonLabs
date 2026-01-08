# Write a program that will take a floating input from the user and will display the integer and the
# fractional part separately.


number = float(input("Enter a floating number: "))
integer_part = int(number)
fractional_part = number - integer_part
print(f"Integer part is: {integer_part}")
print(f"Fractional part is: {fractional_part}")