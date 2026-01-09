"""
 Area of Pentagon:
An irregular pentagon ABCDE is shown here:
To find the area of this pentagon, we can divide the shape into three triangles; ΔABC, ΔACE and
ΔECD as shown below:
Write a program that will ask user to enter five X-Y points and will display the area of the
pentagon made of those. You must do the task by creating following functions:
• dist → It will have four input arguments (2 X-Y Points) and will return the distance
between them.
• triAreaSides →It will have three input arguments and will return the area of the
triangle made of those three points.
• triAreaPoints → It will have six input arguments (3 X-Y Points) and will return the
area of triangle made by those three points using the dist function to calculate three
sides and triAreaSides to calculate the area.
• pentaArea → It will have ten input arguments (5 X-Y Points) and will return the area of
the pentagon made of those points. This function will use triAreaPoints three times
for the three triangle areas as explained above and will return their sum as the area of
the pentagon.
The main program of the task will be as:
### Main Program Starts Below ###
x1,y1=eval(input('Enter 1st Point (Format: a,b) :'))
x2,y2=eval(input('Enter 2nd Point (Format: a,b) :'))
x3,y3=eval(input('Enter 3rd Point (Format: a,b) :'))
x4,y4=eval(input('Enter 4th Point (Format: a,b) :'))
x5,y5=eval(input('Enter 5th Point (Format: a,b) :'))
area=pentaArea(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5)
print(f'The area of pentagon with entered points is: {area}')

"""
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

def pentaArea(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5):
 'Calculates Area of a Pentagon made from five points'
 area1 = triAreaPoints(x1, y1, x2, y2, x3, y3)
 area2 = triAreaPoints(x1, y1, x3, y3, x5, y5)
 area3 = triAreaPoints(x3, y3, x4, y4, x5, y5)
 total_area = area1 + area2 + area3
 return total_area

x1,y1=eval(input('Enter 1st Point (Format: a,b) :'))
x2,y2=eval(input('Enter 2nd Point (Format: a,b) :'))
x3,y3=eval(input('Enter 3rd Point (Format: a,b) :'))
x4,y4=eval(input('Enter 4th Point (Format: a,b) :'))
x5,y5=eval(input('Enter 5th Point (Format: a,b) :'))
area=pentaArea(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5)
print(f'The area of pentagon with entered points is: {area}')

