"""
if(a>=b):
 if(a>=c):
 greatest=a
 else:
 greatest=c
else:
 if(b>=c):
 greatest=b
 else:
 greatest=c
print(str(greatest)+' is the greatest.')
Tasks: Complete the code of above example by taking three numbers from user and printing the number
value instead of a, b or c. Secondly, do it with the first comparison between a and c instead of
a and b
"""

a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
c = float(input("Enter third number (c): "))
if(a>=c):
    if(a>=b):
        greatest=a
    else:
        greatest=b
else:
    if(c>=b):
        greatest=c
    else:
        greatest=b
print(str(greatest)+' is the greatest.')
