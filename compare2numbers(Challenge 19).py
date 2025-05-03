#Ask user for the first number
num1 = float(input("Enter the first number: "))
#Ask user for the second number
num2 = float(input("Enter the second number: "))
#Check if first number is bigger than the second number
if num1 > num2:
    print (num1, " is greater than ", num2)
#Check if first number is less than the second number
elif num1 < num2:
    print (num2, " is greater than", num1)
#If first to criterias are not met, print first umber is equal to the second number
else:
    print (num1, "is equal to", num2)
