import time
k = "'We say Burgers, you say Bobbers!'"
#Store these passwords into the values x and c - 03/05/25
x = "NoPassWordHere"
c = "PassWordHere"
#Ask user to enter the password - 03/05/25
d = str(input("Please enter the system password here: "))
#If password c is entered, then print Bobbers Burgers Welcome message - 03/05/25
if d == c:
    print("Welcome to the 'Bobbers Burgers' warehouse mainframe. " + k)
#Pause for 0.75 seconds - 03/05/25
    time.sleep(0.75)
#Print please remember to log out message - 03/05/25
    print("Please remember to log out. You specifically Mr. Smith.")
#If password x is entered, then print FBI Welcome message - 03/05/25
elif d == x:
    print("Welcome to the FBI serverbase. Please keep this confidential")
#Pause for 0.75 seconds - 03/05/25
    time.sleep(0.75)
#Print please remember to log out message - 03/05/25
    print("Please remember to log out. You specifically Agent Smith.")
#If something else is entered, then print Incorrect password message - 03/05/25
else:
    print("Incorrect Password, Please something else!")
