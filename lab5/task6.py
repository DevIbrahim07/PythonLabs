"""
 Write a program that will take two numbers as input (say a and b) and will show their ratio at
output (a/b). As you know that division by zero is not possible and a run-time error occurs in an
attempt to divide by zero. You have to incorporate this problem in a way that if second number
entered is zero, program should not calculate the ratio; instead it should display a message that
division by zero is not possible.
Docstring for lab5.task6
"""
num1 =int(input("enter num1: "))
num2 = int(input("enter num2: "))
if num2 == 0:
    print("division by zero is not possible")
else:
    num = num1/num2
    print(f"Ratio of two numbers is {num}" )