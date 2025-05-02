import time
#Ask for user's name
x = str(input("What is your name: "))
#Pause for 0.5 seconds
time.sleep(0.5)
#Ask for user's age
d = int(input("How old are you: "))
#Values of each time measurement abriviated 
diy = 365
hid = 24
mih = 60
sim = 60
#Equations to find specific times.
days_alive = d * diy
hours_alive = days_alive * hid
minutes_alive = hours_alive * mih
seconds_alive = minutes_alive * sim
#Print user's name and say how many days, hours, minutes, and seconds they have been alive for
print( str(x) + ", you are: ")
print( f"{days_alive} days")
print( f"{hours_alive} hours")
print( f"{minutes_alive} minutes")
print( f"{seconds_alive} seconds")
