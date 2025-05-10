import turtle
#Ask user what they would like the length of the sides to be - 10/05/25
size = int(input("Enter Length of Triangle..(Anything under 100 is small): "))
#Set up the drawing window - 10/05/25
wn = turtle.Screen()
#Create a turtle - 10/05/25 
tom = turtle.Turtle()
#Define a function that draws an triangle of the given size - 10/05/25
def Triangle(size):
#Repeat steps 3 times as octagon has 3 sides - 10/05/25
    for a in range (3):
#Move the turtle by x amount - 10/05/25
        tom.forward(size)
#Turn the turtle 45 degrees to the right - 10/05/25
        tom.left(120)
#Wait for a mouse or cursor click before closing the window - 10/05/25
    wn.exitonclick()
#Call the function to draw the triangle - 10/05/25
Triangle(size)
