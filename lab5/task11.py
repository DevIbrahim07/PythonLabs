"""
A company insures its employees in the following cases:
• If the employee is married
• If the employee is unmarried, male & above 30 years of age
• If the employee is unmarried, female & above 25 years of age
Write a program which takes marital status, gender and age as input from user. After checking
the given conditions, the output of the program will a message stating whether he/she is eligible
for insurance or not.
"""

marital_status = input("Enter marital status (married/unmarried): ").strip().lower()
gender = input("Enter gender (male/female): ").strip().lower()
age = int(input("Enter age: ").strip())
if marital_status == "married":
    print("The employee is eligible for insurance.")
elif marital_status == "unmarried":
    if gender == "male" and age > 30:
        print("The employee is eligible for insurance.")
    elif gender == "female" and age > 25:
        print("The employee is eligible for insurance.")    
    else:
        print("The employee is not eligible for insurance.")
else:
    print("Invalid marital status entered.")

 