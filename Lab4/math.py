#1 - degree to radians
from math import radians
degree = float(input("Input degree: "))
radian = radians(degree)
print("Output radian:", radian)


#2 - area of a trapezoid
from math import fsum
height = float(input("Height: "))
v1 = float(input("Base, first value: "))
v2 = float(input("Base, second value: "))
areaTrap = 0.5 * fsum([v1, v2]) * height
print("Expected Output:", areaTrap)


#3 - area of a polygon
from math import tan, radians
n = float(input("Input number of sides: "))
lSide = float(input("Input the length of a side: "))
apothem = lSide / (2 * tan(radians(180/n)))
areaPol =  0.5 * n * lSide * apothem
print("The area of the polygon is:", round(areaPol))


#4 - area of a parallelogram
from math import prod
lBase = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
areaPar = prod(lBase, height)
print("Expected output:", areaPar)
