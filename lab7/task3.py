import math 
def distance(x1,y1,x2,y2):
    distanceOfX = (x2 - x1)**2
    distanceOfY = (y2 - y1)**2
    squareRoot = math.sqrt(distanceOfX + distanceOfY)
    return squareRoot

x1, x2 = eval(input("Enter x1 and x2 in (x1, x2) form: "))
y1, y2 = eval(input("Enter y1 and y2 in (y1, y2) form: "))

result = distance(x1,y1,x2,y2)
print(f"the distance between two angles is: {result}")