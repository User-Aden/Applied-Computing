import time
#Ask what is the length of the room is in cm
x = int(input("How long is the length of your room (cm): "))
#Pause for 0.5 seconds
time.sleep(0.5)
#Ask what the width of the room is in cm
d = int(input("How long is the width of your room (cm): "))
#Pause for 0.5 seconds
time.sleep(0.5)
#Find length time width of response
c = x * d
#Print the area of the room is x
print(" The area of the room is " + str(c))
