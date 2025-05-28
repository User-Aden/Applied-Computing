import time
stu_Attendence = 0
attenders = {}
noStudents = int(input('How many students are in your class: '))
time.sleep(0.25)
noPeriods = int(input('How many periods are held in a week(Between 1 - 5): '))
while noPeriods < 1 or noPeriods > 5:
    noPeriods = int(input('Please enter a value between and including numbers 1 - 5: '))
time.sleep(0.25)
for n in range(1, noStudents + 1):
    StuName = input(f'\nWhat is the name of student {n}?: ').strip().capitalize()
    time.sleep(0.25)
    for d in range(1, noPeriods + 1):
        while True:
            period = input(f'\nWas this student in period {d}? (P/A): ').strip().upper()
            if period in ['P', 'A']:
                break
        if period == 'P':
            stu_Attendence =  stu_Attendence + 1
            attenders[StuName] = stu_Attendence    
time.sleep(0.25)
print('\nOverall Attendence Report:\n')
for students, stu_Attendence in attenders.items():
    percent = (stu_Attendence / noPeriods) * 100
    if percent < 75:
        print(str(StuName) + ': ' + str(round(percent, 3)) + '%: This student has attended ' + str(stu_Attendence) + '/' + str(noPeriods) + ' classes this week:---(!Low attendence warning!)')
else:
    print(str(StuName) + ': ' + str(round(percent, 3)) + '%: This student has attended ' + str(stu_Attendence) + '/' + str(noPeriods) + ' classes this week')
