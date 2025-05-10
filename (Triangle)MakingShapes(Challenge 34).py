import turtle
#Ask user what they would like the length of the sides to be
size = int(input("Enter Length of Triangle..(Anything under 100 is small): "))
#Set up the drawing window
wn = turtle.Screen()
#Create a turtle 
tom = turtle.Turtle()
#Define a function that draws an triangle of the given size
def Triangle(size):
#Repeat steps 3 times as octagon has 3 sides
    for a in range (3):
#Move the turtle by x amount
        tom.forward(size)
#Turn the turtle 45 degrees to the right
        tom.left(120)
#Wait for a mouse or cursor click before closing the window
    wn.exitonclick()
#Call the function to draw the triangle
Triangle(size)
