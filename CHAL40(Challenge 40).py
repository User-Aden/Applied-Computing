#Store the name, height and weight of each of the patients in the variable heightandweight - 22/05/25
heightandweight = ['James, 73, 1.82', 'Peter, 78, 1.80', 'Jay', 'Beth, 65, 1.53', 'Mags, 66, 1.50', 'Joy, 62, 1.34']
#Assign the height of x to each patient - 22/05/25
height = { 'James' : 1.82, 'Peter' : 1.80, 'Beth' : 1.53, 'Mags' : 1.50, 'Joy' : 1.34 }
#Assign the weight of x to each patient - 22/05/25
weight = { 'James' : 73, 'Peter' : 78, 'Beth' : 65, 'Mags' : 66, 'Joy' : 62 }
#Open the file CHAL40.txt, and change whatever is in the file to what is bellow - 22/05/25
myFile = open("CHAL40.txt", "w")
#Calculate the sum of all of the height values added together - 22/05/25
TTheight = sum(height.values())
#Caculate the value of all of the weight values added together - 22/05/25
TTweight = sum(weight.values())
#Count the amount of numbers used in height - 22/05/25
amountH = len(height.values())
#Count the amount of numbers used in weight - 22/05/25
amountW = len(weight.values())
#Calculate the average of height of the patients, times by 100 to be converted to cm - 22/05/25
Aheight = (TTheight / amountH) * 100
#Calculate the average of weightof the patients - 22/05/25
Aweight = TTweight / amountW
#In the file, write Patient list, as well as what unformation is included - 22/05/25
myFile.write('Patient List (Name, Weight, Height:\n\n')
#Create a for loop, print all of the patients - as well as their data - into a list, putting each entry onto a new line - 22/05/25
for i in heightandweight:
    myFile.write(str(i) + '\n')
#In the file, write the average height of all patients is x cm, round to 2 decimal places - 22/05/25
myFile.write('\n\nThe average height of all of the patients is: ' + str(round(Aheight, 2)) + ' cm\n\n')
#In the file, write the average weight of all patients is x kilos, round to 3 decimal places - 22/05/25
myFile.write('The average weight of all the patients is: ' + str(round(Aweight, 3)) + ' kilos')
#Close the file - 22/05/25
myFile.close()
