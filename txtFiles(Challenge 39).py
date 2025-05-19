#Store an empty list into the value x - 19/05/25
x = []
#Open the text file named ADEN.txt - 19/05/25
myFile = open("ADEN.txt", "a")
#Repeat the steps bellow 6 times to get 6 numbers for the users - 19/05/25
for a in range (6):
#Ask the user to enter their numbers - 19/05/25 
    newNo = float(input("Please enter new number: "))
#Store the users imputs into the previously made list - 19/05/25
    x.append(newNo)
#Sort all of the values the user input in ascending - 19/05/25
x.sort()
#Print 'This is your sorted list message' inside the txt file - 19/05/25
myFile.write('\nThis is your number list organised in ascending order:\n\n')
#Print all of the users chosen values into the text file - 19/05/25
for i in x:
#Print all of the users inputs into the text files - 19/05/25
        myFile.write(str(i)+"\n")
#Close the file - 19/05/25
myFile.close()
