"""Tasks:
[1] We created these two functions in previous lab:
import math
def dist(x1,y1,x2,y2):
 'Calculates Distance between points (x1,y1) & (x2,y2)'
 d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
 return d
def triAreaSides(a,b,c):
 'Calculates Area of a Triangle with sides a,b and c'
 s=(a+b+c)/2
 a=math.sqrt(s*(s-a)*(s-b)*(s-c))
 return a
Now create another function that will have three X-Y points as input arguments (total six input
arguments) and will use the above two functions to calculate and return the area of the triangle
made from those three points. The structure of the function along with the main program is given
as:
def triAreaPoints(x1,y1,x2,y2,x3,y3):
 'Calculates Area of a Triangle made from three points'
 #Complete the code
### Main Program Starts Below ###
x1,y1=eval(input('Enter 1st Point (Format: a,b) :'))
x2,y2=eval(input('Enter 2nd Point (Format: a,b) :'))
x3,y3=eval(input('Enter 3rd Point (Format: a,b) :'))
area=triAreaPoints(x1,y1,x2,y2,x3,y3)
print(f'The area of triangle with entered points is: {area}')
Consider following steps to complete the code of the function:
• Calculate three sides of the triangle using the dist function and provide 1st and 2nd point
as input, then 1st and 3rd point and then 2nd and 3rd point. So, you will be using the function
dist three times and storing the results in three variables of your choice.
• After the three sides obtained in three variables, use the function triAreaSides and
provide the three variables as input.
• Return the calculated answer from above step."""
import math

def dist(x1,y1,x2,y2):
 'Calculates Distance between points (x1,y1) & (x2,y2)'
 d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
 return d
def triAreaSides(a,b,c):
 'Calculates Area of a Triangle with sides a,b and c'
 s=(a+b+c)/2
 a=math.sqrt(s*(s-a)*(s-b)*(s-c))
 return a

def triAreaPoints(x1,y1,x2,y2,x3,y3):
 'Calculates Area of a Triangle made from three points'
 a = dist(x1, y1, x2, y2)
 b = dist(x1, y1, x3, y3)
 c = dist(x2, y2, x3, y3)
 area = triAreaSides(a, b, c)
 return area
x1,y1=eval(input('Enter 1st Point (Format: a,b) :'))
x2,y2=eval(input('Enter 2nd Point (Format: a,b) :'))
x3,y3=eval(input('Enter 3rd Point (Format: a,b) :'))
area=triAreaPoints(x1,y1,x2,y2,x3,y3)       
print(f'The area of triangle with entered points is: {area}')


