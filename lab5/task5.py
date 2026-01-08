
"""
Write a program that will take a number from user and will display the square root of it.
We can find the square root of the number using sqrt() function in Math module. But if we
try to pass a negative number as input argument, it will generate run-time error. You can check
that as shown here:
>>> import math
>>> sqrt(-4)
And you will see an error something like:
NameError: name 'sqrt' is not defined
But we know that square root of -4 is 2j. So, for this program you will take a number from user
and then apply an if-else statement to check whether input number is positive or negative.
If it is positive, simply use sqrt() and display the result. If entered number is negative, make is
positive, use sqrt() and then display the result appending a 'j' with it.
How to make a negative number a positive equivalent?
If variable a contains a negative number we can use:
a=a*-1
or:
a*=-1
or we can use abs() function as abs(a)
"""
# from math import *
# number = int(input("enter a number: "))
# square_root = round(sqrt(number),2)
# print(f"the square root of this number is {square_root}")

import math 

num = int(input("Enter a number: "))
if num >=0:
    print("the square root is ok")
else:
    num = abs(num)
    print(f"The square root is {math.sqrt(num)}j")