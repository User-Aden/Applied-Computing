import time
#Ask how many people does the user want to share their money with
x = int(input("How many people do you want to share the money with (Including yourself): "))
#Pause for 0.5 seconds
time.sleep(0.5)
#Divide the $1000 dollars by how many people it is to be shared with, and print Each person will get x amount of dollars each
money = 1000 / x
#Print each person will get x amount of money
print("Each person will get $" + str(money) + " each")
