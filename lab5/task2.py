
"""
Write a program that asks the user to enter a length in centimeters. If the user enters a negative
length, the program should tell the user that the entry is invalid. Otherwise, the program should
convert the length to inches and print out the result. There are 2.54 centimeters in an inch.
"""

LengthInCentimeter =eval(input("enter a length in centemeter: "))

if(LengthInCentimeter<0):
    print("entry is invalid")
else:
    LengthInInches = LengthInCentimeter / 2.54
    print(f"{LengthInCentimeter} centemeter is {LengthInInches} inches")
