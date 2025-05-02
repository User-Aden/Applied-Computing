#This code is for the Names.py task. (Challege One)

#Ask for first name 
x = input("What is your first name: ")
#Ask for surname 
d = input ("What is your surname: ")
#Ask for is there a space between first and surname.
c = input("Is there a space between your first and last name (yes/no): ")
Full_name = ( x + ' ' + d)
Full_name2 = ( x + d)
lowerC = c.lower () == "yes"
#If answer was yes, print this:
if c == "yes": 
  print( x + ' ' + d)
  print( d + ' ' + x)
  print(Full_name)
  #If answer was no, print this:
else:
    print( x + d)
    print( d +  x)
    print(Full_name2)
