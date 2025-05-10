import time
#Define the formula of area as length x width - 10/05/25
def area(length, width):
    shapeArea = length * width
    print("\n\nTotal Area = ", str(shapeArea))
#Define the formula of volume as length x width x height - 10/05/25
def volume(length, width, height):
    shapeVolume = length * width * height
    print("\n\nTotal Volume = " + str(shapeVolume))
#Define the formula of perimeter as 2xLength + 2xWidth - 10/05/25
def perimeter(length, width):
    shapePerimeter = 2 * (length + width)
    print("\n\nTotal Perimeter = " + str(shapePerimeter))
#Ask the user the questionuntil, they enter A, P or V - 10/05/25
x = None
while x not in ("A", "P", "V"):
    x = input("Do you want to calculate area, perimeter, or volume? Enter A, P or V: ").capitalize()
#Ask the user to input the length - 10/05/25
length = int(input("Enter the length of the rectangle: "))
#Pause for 0.5 seconds - 10/05/25
time.sleep(0.5)
#Ask the user to input the width - 10/05/25
width = int(input("Enter the width of the rectangle: "))
#If user entered A, use the predefined area - 10/05/25
if x == "A":
    area(length, width)
#If user entered P, use the predefined perimeter - 10/05/25
elif x == "P":
    perimeter(length, width)
#If user entered V, use the predefined volume - 10/05/25
else:
#Pause for 0.5 seconds - 10/05/25
    time.sleep(0.5)
    height = int(input("Enter the height of the rectangle: "))
    volume(length, width, height)
