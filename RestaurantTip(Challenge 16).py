#Ask how many people are there
d = int(input("How may people are you dining with: "))
#Ask how much the bill is
r = float(input("How much is the bill (In dollars): "))
#Ask how much of a tip the users would like to leave
f = float(input("How much of a tip would you like to leave (In percentage): "))
#Ask how far are the users would like to go in the taxi
taxi = float(input("How far are you going to travel in the taxi (In Miles): "))
#Calculate taxi fee by timesing the taxi fare by the amount of miles they will travel
taxiFee = 0.45 * taxi
#Convert the percentage into a decimal
tipAmount = f / 100
#Find how much the total tip is
tip = r * tipAmount
#Divide the bill by the amount of people present
bill = r / d
#Divide the total tip by the amount of people dining
tip2 = tipAmount / d
#Add all the costs together.
Total_bill = tip2 + bill + taxiFee
#Round to two decimal places
FinalBill = (str(Total_bill)[:5])
#Print total cost per person (assuming they split everything) for the night
print("For the whole evening, if everyone splits the bill evenly, each person would pay $" + FinalBill + " each.")
