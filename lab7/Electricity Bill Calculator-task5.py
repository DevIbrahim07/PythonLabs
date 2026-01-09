# Electricity Bill Calculator:
"""Now you have to do the same task but using a function named as billElect(u) to calculate
the amount of bill. In the main program you will be taking the number of units consumed, then
use the function and simply display the result. All required calculations will be done in the
function block. Also return the bill which will be charged after the due date.
The main code with function declaration is given as:
"""
units_Consumed=eval(input("Enter Electricity Units Consumed: "))
def billElect(u):
 if u<=100:
    Amount = u * 13.85
 elif(100<u<=200):
   Amount = u * 15.86
 elif(200<u<=300):
    Amount = u * 16.83
 elif(300<u<=700):
   Amount = u * 18.54
 elif(u>700):
    Amount = u * 20.94

 Neelum_Jhelum_Surcharge = 0.1
 Financial_Cost_Surcharge =0.43
 Tv_Charges = 35
 Total_Amount = Amount +Neelum_Jhelum_Surcharge + Financial_Cost_Surcharge + Tv_Charges 
 Gst = Total_Amount * 0.12
 Total_bill= Total_Amount + Gst
 Late_Payment_Charge = Total_bill * 0.0834
 Bill_After_Due_Date = Total_bill + Late_Payment_Charge
 print("Total Bill Payable within Due Date is: ", round(Total_bill,2))
 print("Total Bill Payable after Due Date is: ", round(Bill_After_Due_Date,2))
 


billElect(units_Consumed)

