import time
#Ask what user wants most for chritmas
x = str(input( "What would you like for christmas most: "))
#Pause for 0.5 seconds
time.sleep(0.5)
#Ask what else user wants for christmas 
d = str(input( "What else would you like for christmas: "))
#Pause for 0.5 seconds
time.sleep(0.5)
#Ask for one more thing user wants for christmas
c = str(input( "What is one more thing you would like for christmas: "))
#Pause for 0.5 seconds
time.sleep(0.5)
#Put all gifts in a sentence and print it
all_gifts = x + ", " + d + ", " + c
print(all_gifts)
