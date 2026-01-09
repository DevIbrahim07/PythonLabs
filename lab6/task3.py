"""
Continuing the same previous problem, if the user is married, he/she is eligible for insurance
regardless of the gender and age. So, if a person is married, the program should not ask for
gender and age. 
"""
status = input("Enter your marital status (M/U): ")
if(status=='M' or status=='m'):
    print('Congratulations! \nYou are eligible for the insurance.')
else:
    gender = input("Enter your gender (M/F): ")
    age=eval(input("Enter your age: "))
    if(gender=='M' or gender=='m'):
        
        if(age>30):
            print('Congratulations! \nYou are eligible for the insurance.') 
        else:
            print('Sorry! \nYou are not eligible for the insurance.')