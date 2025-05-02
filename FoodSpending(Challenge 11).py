import time
#Ask how much the user spends on lunchtime food in a average day
x = float(input("How much do you spend on lunchtime food in an average day? "))
#Pause for 0.5 seconds
time.sleep(0.5)
x = x *5
print ("This means that in a week you will spend: $" + str(x) + " on lunchtime foods." )  
