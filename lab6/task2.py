"""
Complete the task 11 of last lab session using nested if-else statement. A starting logic is
given at the end:
A company insures its employees in the following cases:
• If the employee is married
• If the employee is unmarried, male & above 30 years of age
• If the employee is unmarried, female & above 25 years of age
Write a program which takes marital status, gender and age as input from user. After checking
the given conditions, the output of the program will a message stating whether he/she is eligible
for insurance or not.


"""
status = input("Enter your marital status (M/U): ")
gender = input("Enter your gender (M/F): ")
age=eval(input("Enter your age: "))
if(status=='M' or status=='m'):
    print('Congratulations! \nYou are eligible for the insurance.')
else:
    if(gender=='M' or gender=='m'):
        
        if(age>30):
            print('Congratulations! \nYou are eligible for the insurance.') 
        else:
            print('Sorry! \nYou are not eligible for the insurance.')
    else:
        
        if(age>25):     
            print('Congratulations! \nYou are eligible for the insurance.')
        else:
            print('Sorry! \nYou are not eligible for the insurance.')


