"""
Write a program that will take a three-digit number as input and will display three digits
separately in a column and show their sum.
"""

number = int(input("Enter a 3-digit number: "))
unit = number % 10
number //= 10
tenth = number % 10
hundredth = number // 10
print(f"{hundredth}\n{tenth}\n{unit}")
print(f"{hundredth} + {tenth} + {unit} = {hundredth + tenth + unit}")

