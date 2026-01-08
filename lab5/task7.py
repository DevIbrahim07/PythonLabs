"""
perfect square is the one whose square-root is an integer e.g. 16 is perfect square and 15 is
not. Write a program that will take a number from user and will display whether it is perfect
square or not.

"""
import math
num = int(input("Enter a number: "))
root = int(math.sqrt(num))
if (root** root ==num):
    print("this is perfect square root")
else:
    print ( "this is not a perfect square root")