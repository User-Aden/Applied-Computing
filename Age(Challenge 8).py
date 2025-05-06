import time
#Ask for user's name
x = str(input("What is your name: "))
#Pause for 0.5 seconds
time.sleep(0.5)
#Ask for user's age
d = int(input("How old are you: "))
#Equations to find specific times.
days_alive = d * 365
hours_alive = days_alive * 24
minutes_alive = hours_alive * 60
seconds_alive = minutes_alive * 60
#Print user's name and say how many days, hours, minutes, and seconds they have been alive for
print( str(x) + ", you are: ")
print( f"{days_alive} days")
print( f"{hours_alive} hours")
print( f"{minutes_alive} minutes")
print( f"{seconds_alive} seconds")
