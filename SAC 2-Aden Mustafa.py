import time
noStudents = int(input('How many students are in your class: '))
time.sleep(0.25)
noPeriods = int(input('How many periods are held in a week: '))
time.sleep(0.25)
for n in range(1, noStudents + 1):
    while True:
        StuName = input(f'What is the name of student {n}?: ').strip().capitalize()
time.sleep(0.25)
for d in range(1, noPeriods + 1):
    while True:
        period = input(f'\nWas this student in period {d}? (P/A): ').strip().upper()
        if period in ['P', 'A']:
            break  

