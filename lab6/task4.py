"""
Write a program that will ask user to enter day and month (e.g. day=7 and month=3). At output
the program should display the next day. We will assume that user will always enter a valid
date.
d=eval(input("Enter Day: "))
m=eval(input("Enter Month: "))
if(d<=27 or d==29):
 nextDay=d+1
else:
 if(d==28 and m==2):
 nextDay=1
 if(d==28 and m!=2):
 nextDay=29
 if(d==31):
 nextDay=1
 if() # if for d=30 and month with 30 days
 if() # if for d=30 and month with 31 days
print('The next day is : '+str(nextDay))
Following points must be noted in above logic:
• The next day generally is entered day plus one except for the cases when it is the last day
of a month; then the next day will be 1.
• Last day of a month varies for different months. It can be 28 (For February), 30 (For April,
June, September and November) or 31 (For January, March, May, July, August, October
and December).
• Based on above rule, if day is less than or equal to 29 but not 28, then the next day is
surely current day plus one. Therefore, we have the first if statement condition.
• The else of first if statement will be active when condition is false i.e. current day is
28, 30 or 31. It is handled as described below:
▪ First two ifs' are for 28 days with month being February or other.
▪ Third if is for 31 days and for that the next day is always 1st of next month.
▪ Fourth and fifth ifs' are for 30 days; one for the months with 30 days having the
next day as 1 and other for the months with 31 days having the next day as 31.
• After the whole calculations, final display statement is used. You must note that this
statement is outside of the if and else block.
• Last point to be noted is that in the else block of the first if statement, the five ifs'
are not nested within each other rather those five ifs' are independent. All those five
7 | P a g e
ifs' will be checked (given the code enters into else block) even if the first gets true.
But the conditions of those ifs' are such that only one can be true.


"""
d = eval(input("Enter Day: "))
m = eval(input("Enter Month: "))
if (d <= 27 or d == 29):
    nextDay = d + 1
else:
    if (d == 28 and m == 2):
        nextDay = 1
    if (d == 28 and m != 2):
        nextDay = 29
    if (d == 31):
        nextDay = 1
    if (d == 30 and m in [4, 6, 9, 11]):
        nextDay = 1
    if (d == 30 and m in [1, 3, 5, 7, 8, 10, 12]):
        nextDay = 31
print('The next day is : ' + str(nextDay))

