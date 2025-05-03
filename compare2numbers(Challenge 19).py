# Ask user for the first number - 03/05/25
num1 = float(input("Enter the first number: "))
# Ask user for the second number - 03/05/25
num2 = float(input("Enter the second number: "))
# Check if first number is bigger than the second number - 03/05/25
if num1 > num2:
    print(num1, "is greater than", num2)
# Check if first number is less than the second number - 03/05/25
elif num1 < num2:
    print(num2, "is greater than", num1)
# If first two criteria are not met, print first number is equal to the second number - 03/05/25
else:
    print(num1, "is equal to", num2)
