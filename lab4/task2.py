# fstring formating
x = 100000
print(f"{x:,}")
# round off function
b = 2.33333
print(round(b))
print(round(b,3))

"""
 Upgrade the Task 2 using the appropriate number formatting described in above table so that
colon (:) is printed using the formatting and both minutes and seconds are displayed in 2-digits
and hours are displayed with 2 or more digits.
"""
from math import *
input_Time = eval(input("enter a time in seconds: "))
hours = input_Time // 3600
minutes = (input_Time % 3600) // 60
seconds = input_Time % 60
print(f" {hours:0>2}:{minutes:0>2}:{seconds:0>2}")