import time
#Store all of the values in a dictionary - 16/05/25
countryPop = {"JAPAN": "127000000", "GERMANY": "81000000", "IRAN": "77000000", "UK": "64000000", "CANADA": "33000000", "AUSTRALIA": "23000000", "USA": "317000000", "BULGARIA": "7000000", "SWEDEN": "10000000"}
#Pause for 0.5 seconds - 16/05/25
time.sleep(0.5)
#Print the welcome message - 16/05/25
print('Welcome to Country Counter!')
#Pause for 0.5 seconds - 16/05/25
time.sleep(0.5)
#Print what the Country Counter does - 16/05/25
print('Where you can add the population of two countries together.')
#Pause for 1.15 seconds - 16/05/25
time.sleep(1.15)
#Ask the user what their first counrty is - 16/05/25
x = str(input('\nWhat is your first country: ')).strip().upper()
while x not in countryPop:
    x = input("You may have misspelled that; What is your first counrty: ").strip().upper()
#Pause for 0.5 seconds - 16/05/25
    time.sleep(0.5)
#Ask the user what their second counrty is - 16/05/25
d = str(input('You may have misspelled that; What is your second country: ')).strip().upper()
while d not in countryPop:
#Pause for 0.5 seconds - 16/05/25
        time.sleep(0.5)
        d = str(input('What is your second country: ')).strip().upper()
#If the both values are valid, add he population of the two countries - 16/05/25
c = int(countryPop [x]) + int(countryPop [d])
#Pause for 0.5 seconds - 16/05/25
time.sleep(0.5)
#Print the total population of the two countries combined is x amount - 16/05/25
print('The total population of the two counties combined is: ' + str(c) + ' people!')
