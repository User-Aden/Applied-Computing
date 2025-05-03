import time
import math

# Ask user how many pictures they would like to send this month - 03/05/25
x = float(input("How many pictures would you like to send this month (they cost $0.35 each): "))
# Pause for 0.5 seconds - 03/05/25
time.sleep(0.5)
# Ask user how many texts they would like to send this month - 03/05/25
d = float(input("How many texts would you like to send this month (they cost $0.10 each): "))
# Pause for 0.5 seconds - 03/05/25
time.sleep(0.5)
# Ask user how much data they would like to use this month (in MBs) - 03/05/25
c = float(input("How much data would you like to use this month (in MBs): "))
# Pause for 0.5 seconds - 03/05/25
time.sleep(0.5)
# Calculate the cost of every price: times the amount of pictures, texts, and data by their respective prices - 03/05/25
pic = x * 0.35
text = d * 0.10
data500MB = math.ceil(c / 500)
data = data500MB * 2.50
# Add all the prices up - 03/05/25
bill = pic + text + data
# Print the cost of the bill - 03/05/25
print("\nThe total cost of your phone bills this month comes to $" + str(round(bill, 2)))
# Pause for 0.75 seconds - 03/05/25
time.sleep(0.75)
# If the bill is greater than $10.0, suggest the contract - 03/05/25
if bill > 10:
    print("\n\nYour total cost is greater than $10.0, you could be getting better value if you switched to the contract!")
