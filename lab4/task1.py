x = "10"
y = float(x)+5
print(x,y)
print("5+5 =" ,10)
print("5+5 =" + 10)
print("5+5 = " + str(10))
print("5+5 = " , str(10))
# # multiline statements using backword slash \ 
num1= 30
num2 = 30
num3 = 40
total = num1 + \
num2 + \
num3
print(total)
# # by also using indentation for better code
num1= 30
num2 = 30
num3 = 40
total = num1+ \
        num2+ \
        num3
print(total)

# Write a program that will ask user for the number of seconds and will print out that time in
# MM:SS format i.e. Minutes:Seconds
from math import *
input_Time = eval(input("enter a time in seconds: "))
hours = input_Time // 3600
minutes = (input_Time % 3600) // 60
seconds = input_Time % 60
print(f" {hours}: {minutes} : {seconds}")