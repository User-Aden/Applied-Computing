import turtle 
#Ask user what they would like the length of the sides to be
size = int(input("Enter Length of Octagon..(Anything under 100 is small): "))
#Set up the drawing window
wn = turtle.Screen()
#Create a turtle 
tom = turtle.Turtle() 
#Define a function that draws an octagon of the given size
def Octagon(size):
#Repeat steps 8 times as octagon has 8 sides
    for a in range(8):
#Move the turtle by x amount
        tom.forward(size)
#Turn the turtle 45 degrees to the right
        tom.right(45)
#Wait for a mouse or cursor click before closing the window
    wn.exitonclick()
#Call the function to draw the octagon
Octagon(size)
