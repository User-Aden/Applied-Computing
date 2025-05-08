import time
#Ask the user for what times tables they would like to know.
x = int(input("Enter a number for the times table: "))
#Pause for 0.5 seconds
time.sleep(0.5)
#Print the users input + Times table
print("\n",x, "Times table's:\n")
#Pause for 0.5 seconds
time.sleep(0.5)
#Print out the the numbers from 1 to 13 for d
for d in range(1, 13):
#Print user input times 1-12 = x times d
    print(str(x) + " x " + str(d) + " = " + str(x * d))
#Pause for 0.10 seconds
    time.sleep(0.10)
