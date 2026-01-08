x = 3+4j
print(x)
y=complex(3,4)
print(y)
# two complex number from user and their product
num1 = complex(eval(input("enter first complex number: ")))
num2 = complex(eval(input("enter second complex number: ")))
result = num1*num2
print(f"total product is: {result}")

# magnitude of number by using abs() function
num = abs(-4)
print(f"the magnitude of number is: {num}")
x=4+3j
y=abs(x)
print(y)
x=5+4j
a=x.real
b=x.imag
print(f"real part is: {a}")
print(f"imaginary part is: {b}")


"""
 Write a program that will input a complex number and will display the magnitude of that. Do not
use abs() function to find the magnitude; instead, get the real and imaginary part of the
entered complex number and calculate the magnitude using this formula:
|𝑥| = √(𝑅𝑒𝑎𝑙)
2 + (𝐼𝑚𝑎𝑔)
2
Use proper number formatting so that only two digits after decimal points are displayed.
"""
from math import *
num =complex(eval(input("enter complex number: ")))
real = num.real
imagenary = num.imag
result = sqrt((real**2)+(imagenary**2))
print(f"the magnitude of entered number is: {result:.2f}")