"""
 Electricity Bill Calculator: Electricity Bills are calculated on the basis of Units (KWhr) used. The
LESCO tariffs for domestic users are given as:
Description Rates
For first 100 Units 13.85 Rs/Unit
101-200 Units 15.86 Rs/Unit
201-300 Units 16.83 Rs/Unit
301-700 Units 18.54 Rs/Unit
Above 700 Units 20.94 Rs/Unit
Neelum Jhelum Surcharge
NJ-Sur 0.1 Rs/Unit
Financial Cost Surcharge
FC-Sur 0.43 Rs/Unit
TV Charges (Fix) 35 Rs
GST 12% of Calculated amount
Write a program that will ask user to enter number of electricity units consumed and will show
the amount of bill at output. LESCO charges extra 8.34% of total amount if bill is not paid within
due date. The program should display the amount of bill payable within due date and after due
date. Use elif instead of else if.

"""

units_Consumed =int(input("enter electricity units consumed: "))
# Calculating Amount based on units consumed
if units_Consumed<=100:
    Amount = units_Consumed * 13.85
elif(100<units_Consumed<=200):
   Amount = units_Consumed * 15.86
elif(200<units_Consumed<=300):
    Amount = units_Consumed * 16.83
elif(300<units_Consumed<=700):
   Amount = units_Consumed * 18.54
elif(units_Consumed>700):
    Amount = units_Consumed * 20.94

# Surcharge
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


