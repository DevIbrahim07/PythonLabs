"""Write a function named as triAreaSides that will calculate the area of a triangle from three
sides."""
import math
def triAreaSides (sideA,sideB,sideC):
    sides = (sideA+sideB+sideC)/2
    area = math.sqrt(sides*(sides-sideA)*(sides-sideB)*(sides-sideC))
    return area

sideA = float(input("enter side a: "))
sideB = float(input("enter side b: "))
sideC = float(input("enter side c: "))
totalArea = triAreaSides(sideA,sideB,sideC)
print(totalArea)
