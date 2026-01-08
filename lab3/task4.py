import math
print(dir(math))
print(help(math.sqrt))
print(help(math))
from math import sqrt,exp
x = eval(input("enter the number: "))
a = sqrt(x)
print(f"the square root of {x} is {a}")
import math
# from math import *
x = eval(input("enter number: "))
a = math.sqrt(x)
print(f"the square root of {x} is {a}")
"""
A Cultural Musical Concert is being held in Al-hamra Complex. There are three seating categories in
the hall. Class A gallery seats cost Rs. 1000, Class B gallery seats cost Rs. 700 and Class C gallery seats
cost Rs. 500. Write a program that asks how many tickets for each class of seats were sold, then
displays the amount of income generated from ticket sales. 

"""
from math import *
classA = 1000
classB = 700
classC = 500
a = int(input("enter number of tickets sold for clss A: "))
b= int(input("enter number of tickets sold for clss B: "))
c = int(input("enter number of tickets sold for clss C: "))
income = (a*classA)+(b*classB)+(c*classC)
print(f"the total income generated form tickets is Rs.{income}")