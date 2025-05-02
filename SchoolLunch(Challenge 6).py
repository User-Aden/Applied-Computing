import time
#Ask how much money did you start they day off with
x = int(input("How much money did you start today with: "))
#Pause for 0.5 seconds
time.sleep(0.5)
#Ask how much money did you spend today
h = int(input("How much money did you spend today: "))
#Subtract starting amount of money by amount spent
d = x - h
#Pause for 0.5 seconds
time.sleep(0.5)
#If result is greater than or equal to 0, print (You have x amount left)
if d >= 0:
    print("You have $" + str(d) + " left.")
#If result is less than or equal to 0, print( You have gone x amount into debt
if d < 0:
    print("You have gone $"+ str(d) + " into debt.")
