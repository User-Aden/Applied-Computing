import time
#Print the title of Candy Bar list - 14/05/25
print('Candy Bar List:\n')
#Pause for 0.75 seconds - 14/05/25
time.sleep(0.75)
#Store the list of candy bars inside of candyTT - 14/05/25
candyTT = ["Mars", "Bounty", "Twix"]
#Pause for 0.20 seconds - 14/05/25
time.sleep(0.20)
#Add the value KitKat to the list - 14/05/25
candyTT.append("KitKat")
#Add the value Snickers to the list - 14/05/25
candyTT.append("Snickers")
#Add the value Horn into the one space - 14/05/25
candyTT.insert(1, "Horn")
#Add the two values Picnic and Twirl to the list - 14/05/25
candyTT.extend(["Picnic", "Twirl"])
#Print the list of values - 14/05/25
for i in candyTT:
#Pause for 0.20 seconds - 14/05/25
    time.sleep(0.20)
    print(i)
