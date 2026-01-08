"""
 Repeat task 4 but this time use the conjugate function of complex class to calculate the
magnitude. A complex number when multiplied with its conjugate gives the square of the
magnitude of that complex number.
Note→ While attempting to find the square-root of the product of the number and the conjugate,
you will get an error as sqrt() function cannot be applied to a complex number. The imaginary
part of the product is 0 but still it is a complex number. So use the real part of the product in
sqrt() function. 
"""

from math import *
num =complex(eval(input("enter complex number: ")))
real = num.real
imagenary = num.imag
conjugate = complex(real, -imagenary)
product = num * conjugate
result = sqrt(product.real)
print(f"the magnitude of entered number is: {result:.2f}")