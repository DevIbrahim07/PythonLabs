"""
DocWrite a program that asks the user for an hour between 1 and 12, and then asks them to enter
am or pm. The program then shows the hour in 24-Hour format.Before you proceed for the logic it is important to understand the 12:00 Noon confusion. Is it
12am or 12pm at noon? Generally, we consider 12:00pm as noon and 12:00am as midnight. But
the fact is 12am and 12pm both are true for midnight and it's 12:00m for the 12:00 noon. For
simple logic here we will assume 12:00am as 12:00 Noon and 12:00pm as 12:00 midnight.
Therefore, if user enters am, the same hour will be in 24-hours format and otherwise i.e. for pm
it will be entered hour plus 12.
"""

hour = int(input("enter hour bertween 1 and 12: "))
am_pm = input ("enter am or pm: ").strip().lower()
if am_pm == "am":
    if hour == 12:
        hour_24 = 0
    else:
        hour_24 = hour
else:
    if hour ==12:
        hour_24 = 12
    else:
        hour_24 = hour + 12
print("Hour in 24-hour format is:", hour_24)
    
