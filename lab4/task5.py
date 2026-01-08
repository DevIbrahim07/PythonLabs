"""
Write a program that will take input a vector (in form of complex number) from user and will
display the unit vector (in form of complex number) of that.
Use proper number formatting so that only two digits after decimal points are displayed.
"""
from math import *
num = complex(input("enter complex number: "))
real = num.real
imagenary = num.imag
magnitude = sqrt((real**2)+(imagenary**2))
unit_real = real / magnitude
unit_imaginary = imagenary / magnitude
unit_vector = complex(unit_real, unit_imaginary)
print(f"the unit vector is: {unit_vector.real:.2f}{unit_vector.imag:.2f}j")