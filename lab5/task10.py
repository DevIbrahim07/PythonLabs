"""
 Write a program that will take three numbers as input and will print the maximum of three
numbers at output. You have to use three if statements.
"""
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
max_num = num1
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3
print("The maximum number is:", max_num)
