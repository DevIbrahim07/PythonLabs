"""
 In last lab you did a task to take input three sides of a triangle and show the area of triangle. We
assumed that user will always enter a valid triangle. As we know that for a valid triangle the
condition is that sum of any two sides should be greater than the third one. Now update that
program such that it takes three sides as input and will print the area only if it is a valid triangle
otherwise it should print that triangle is invalid.

"""
import math
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"The area of the triangle is: {area}")
else:
    print("The triangle is invalid.")
    

