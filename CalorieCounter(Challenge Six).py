#Print users calorie counter
print("Aden’s calorie counter")
#Ask how many calories have you eaten today
d = int(input("How many calories have you eaten today? "))
#Minus the amount of calories given by set amount (2000)
x =2000-d
#If remaining calories  bigger than 0, print you can eat x amount more calories today
if x > 0:
    print("You can eat", x, "more calories today")
#If remaining calories equal to 0, print you can eat no more calories today
if x == 0:
        print("You can eat no more calories today")
#If remaining calories less than 0, print you overate on calories today
if x < 0:
    print("You overate on calories today")

