import time
#Ask on a scale of 1 to 10, how are they feeling - 03/05/25
x = int(input("On a scale of 1 to 10 how are you feeling (In number form please): "))
#Pause for 0.55 seconds - 03/05/25
time.sleep(0.55)
#If x is less than or equal to 3, print Hang in there message - 03/05/25
if x <= 3:
    print("Hang in there, tommorow is a new day!")
#If x is between, and including 4 to 7, print Keep you head high champ message - 03/05/25
elif 4 <= x <= 7:
    print("Not too shabby, keep your head high champ!")
#If x is greater than or equal to 8, print Spread this joy you're feeling  - 03/05/25
elif x >= 8:
    print("That's great to hear! Spead this joy you're feeling!")
#If response is not valid, print Please select a number between, and including 1 to 10
else:
    print("Please enter a number that between, and including, 1 to 10")
