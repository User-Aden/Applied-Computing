#Ask the user for the first number
num1 = float(input("Enter the first number: "))
#Ask the user for the second number
num2 = float(input("Enter the second number: "))
#See which is true, then print x depending on what is true
if num1 > num2:
    print (num1, " is greater than ", num2)
elif num1 < num2:
    print (num2, " is greater than", num1)
elif num1 == num2:
    print (num1, "is equal to", num2)
