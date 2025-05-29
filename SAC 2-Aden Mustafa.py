import time
#Create a blank list - 29/05/25 - 12:59pm
attenders = {}
#Ask the user for how many students are in their class - 29/05/25 - 1:00pm
noStudents = int(input('How many students are in your class: '))
#Pause for 0.25 seconds - 29/05/25 - 1:00pm
time.sleep(0.25)
#Ask the user for how many periods of this subject are being held within a week - 29/05/25 - 1:02pm
noPeriods = int(input('How many periods are held in a week(Between 1 - 5): '))
#If the asnwer is less than 1 or greater than 5, ask the slightly modified question - 29/05/25 - 1:02pm
while noPeriods < 1 or noPeriods > 5:
    noPeriods = int(input('Please enter a value between and including numbers 1 - 5: '))
#Pause for 0.25 seconds - 29/05/25 - 1:02pm
time.sleep(0.25)
#For the value of {n}, scale it up by one every time this question is asked, until it is the same number as the amount of students in the user's class - 29/05/25 - 1:04pm 
for n in range(1, noStudents + 1):
#Ask the user what the name of student (number) is - 29/05/25 - 1:05pm
    StuName = input(f'\nWhat is the name of student {n}?: ').strip().capitalize()
#Pause for 0.25 seconds - 29/05/25 - 1:06pm
    time.sleep(0.25)
#Set the variable of stu_Attendence to be 0, and reset to 0 everytime a new students name is entered - 29/05/25 - 1:06pm
    stu_Attendence = 0
#For the value of {n}, scale it up by one every time this question is asked, until it is the same number as the amount of periods the user entered - 29/05/25 - 1:07pm
    for d in range(1, noPeriods + 1):
#While the value entered is = P or A, go to the next question. If the answer is not = P or = A, ask the question until a valid respons is put in - 29/05/25 - 1:08pm
        while True:
            period = input(f'\nWas this student in period {d}? (P/A): ').strip().upper()
            if period in ['P', 'A']:
                break
#If the user input is P, add 1 to stu_Attendence - 29/05/25 - 1:10pm
        if period == 'P':
            stu_Attendence =  stu_Attendence + 1
#Enter the inputed information under the dictionary term of the students name, and store the dictionary information - 29/05/25 - 1:14pm
    attenders[StuName] = stu_Attendence
#Pause for 0.25 seconds - 29/05/25 - 1:14pm
    time.sleep(0.25)
#Save the input history in the variable - 29/05/25 - 1:25pm
file_organise = ""
#Print the title of Overall Attendence Report - 29/05/25 - 1:15pm
print('\nOverall Attendence Report:\n')
file_organise += '\nOverall Attendence Report:\n'
#For each of the terms in the dictionary do the following - 29/05/25 - 1:16pm
for students, stu_Attendence in attenders.items():
#To find the percentage of attendence by dividing the number of P's by the amount of periods, then times it by 100 - 29/05/25 - 1:17pm
    percent = (stu_Attendence / noPeriods) * 100
#If the percentage is less than 75%, then print the first response, if not, print the second response - 29/05/25 - 1:17pm
    if percent < 75:
        print(str(students) + ':\n' + str(round(percent, 3)) + '%: This student has attended ' + str(stu_Attendence) + '/' + str(noPeriods) + ' classes this week:---(!Low attendence warning!)')
        file_organise += str(students) + ':\n' + str(round(percent, 3)) + '%: This student has attended ' + str(stu_Attendence) + '/' + str(noPeriods) + ' classes this week:---(!Low attendence warning!)'
    else:
        print(str(students) + ':\n' + str(round(percent, 3)) + '%: This student has attended ' + str(stu_Attendence) + '/' + str(noPeriods) + ' classes this week')
        file_organise += str(students) + ':\n' + str(round(percent, 3)) + '%: This student has attended ' + str(stu_Attendence) + '/' + str(noPeriods) + ' classes this week\n'
#Create the file 'ClassAttendenceRecords.txt' and change the file contents everytime this python code is completed - 29/05/25 - 1:26pm
with open("ClassAttendenceRecords.txt", "w") as myFile:
#Print eh input history into the file - 29/05/25 - 1:26pm
    myFile.write(file_organise)


