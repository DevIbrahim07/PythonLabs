
"""
Write a program that asks the user for two numbers and prints ' Entered numbers are Closed!',
if the numbers differ within 10 units from each other and prints 'Entered numbers are Not
Closed!' otherwise. Use if-else statement
Docstring for lab5.task3
"""
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
if abs(num1 - num2)<=10:
    print("enter numbers are closed!")
else:
    print("entered numbers are not closed!")