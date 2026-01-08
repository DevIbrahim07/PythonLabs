"""
 Write a program that will ask for the marks of five subjects one by one and will print the average
of the marks. Moreover, a message will be printed out depending upon average marks as:
If average is greater than or equal to 80 → You are an outstanding student.
If average is greater than or equal to 70 but less than 80 → You are a good student.
If average is greater than or equal to 60 but less than 70 → You are an average student.
If average is greater than or equal to 50 but less than 60 → You are a below-average student.
If average is greater than or equal to 40 but less than 50 → You are a poor student.
If average is less than 40→ You need extra ordinary efforts
Max marks are 100 and you can assume that user will enter valid numbers.
"""


s1 = int(input("Enter marks for subject 1: "))
s2 = int(input("Enter marks for subject 2: "))
s3 = int(input("Enter marks for subject 3: "))
s4 = int(input("Enter marks for subject 4: "))
s5 = int(input("Enter marks for subject 5: "))
avg = (s1+s2+s3+s4+s5)/5
max_marks = 100
if avg>=80:
    print("You are an outstanding student.")
if avg>=70 and avg<80:
    print("You are an good student.")
if avg>=60 and avg<70:
    print("You are an average student")
if avg>=50 and avg<60:
    print("You are a below-average student")
if avg>=40 and avg<50:
    print("You are a poor student")
if avg<40:
    print("You need extra ordinary efforts")
