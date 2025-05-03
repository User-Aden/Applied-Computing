#Ask the user for the first number - 03/05/25
num1 = float(input("Enter the first number: "))
#Ask the user for the second number - 03/05/25
num2 = float(input("Enter the second number: "))
#See which is true, then print x depending on what is true - 03/05/25
if num1 > num2:
    print(num1, "is greater than", num2)
#Check if second number is greater - 03/05/25
elif num1 < num2:
    print(num2, "is greater than", num1)
#If both numbers are equal - 03/05/25
elif num1 == num2:
    print(num1, "is equal to", num2)
