"""
There are always multiple ways to implement a logic. In above task we started on the basis of
days first, followed by the month conditions. There can be another logic for the above program
that starts with the month first and then checks for the day. Complete the program given below
for the same task:
d=eval(input("Enter Day: "))
m=eval(input("Enter Month: "))
if(m==2):
 #Complete the logic for month February
if(m==4 or m==6 or m==9 or m==11):
 #Complete the logic for months with 30 days
if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
 #Complete the logic for months with 3 days

"""
d = eval(input("Enter Day: "))
m = eval(input("Enter Month: "))
if (m == 2):
    if (d <= 27):
        nextDay = d + 1
    elif (d == 28):
        nextDay = 1
    elif (d == 29):
        nextDay = 1
elif (m == 4 or m == 6 or m == 9 or m == 11):
    if (d <= 29):
        nextDay = d + 1
    elif (d == 30):
        nextDay = 1
elif (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
    if (d <= 30):
        nextDay = d + 1
    elif (d == 31):
        nextDay = 1
print('The next day is : ' + str(nextDay))
        

