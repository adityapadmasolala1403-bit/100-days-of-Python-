print("==========POLYGON AREA CALCULATOR===========")


print("AREA OF SQUARE CALCULATOR")
a=float(input("Enter the side length of square:"))
area=a**2
print("Area of Square with side legth",a,"is",area)

print("AREA OF RECTANGLE CALCULATOR")
b=float(input("Enter the breadth of rectangle:"))
h=float(input("Enter the height of rectangle:"))
area=b*h
print("Area of the rectangle is:",area)

print("AREA OF TRAPEZOID CALCULATOR")
a=float(input("Enter the 1st side length:"))
b=float(input("Enter the 2nd side length:"))
h=float(input("Enter the height of trapezoid:"))
area=((a+b)*h)/2
print("Area of trapezoid:",area)

print("TRIANGLE AREA CALCULATOR")
b=float(input("Enter the base of triangle:"))
h=float(input("Enter the height of triangle:"))
area=(b*h)/2
print("Area of triangle:",area)

print("CIRCLE AREA CALCULATOR")
r=float(input("Enter the radius of circle:"))
a=3.14
area=a*(r**2)
print("Area of circle:",area)
