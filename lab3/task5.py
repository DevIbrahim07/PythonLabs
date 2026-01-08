"""
Write a program that will take three sides of the triangle as input and will display the area of the
triangle at the output using heros formula. If a, b and c are sides of triangle, area of the triangle is:
𝐴𝑟𝑒𝑎 = √𝑠(𝑠 − 𝑎)(𝑠 − 𝑏)(𝑠 − 𝑐)
𝑠 = 𝑎 + 𝑏 + 𝑐

"""
from math import *
a,b,c = eval(input("enter three sies of triangle: "))
s = (a+b+c)/2
area = sqrt((s*(s-a)*(s-b)*(s-c)))
print(f"the area of the triangle is {area}")