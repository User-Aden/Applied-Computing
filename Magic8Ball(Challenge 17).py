import random
import time
 #All possible options the random generator can pick
answer1=("Absolutely!")
answer2=("No way Pedro!")
answer3=("Go for it tiger.")
answer4=("Wait some time")
answer5=("Maybe")
#Print welcome message
print("Welcome to the Magic 8 Ball game—use it to answer your questions...")
 #Ask user to type out their question
question = input("Ask me for any advice and I’ll help you out.  Type in your question and then press Enter for an answer.  ")
 #Print shaking.... x4
print("shaking.... \n" * 4)
time.sleep(1)
#Pick a random number
choice=random.randint(1,5)
#This is what each of the numbers coralate to
if choice == 1:
	answer=answer1
elif choice == 2:
	answer=answer2
elif choice == 3:
	answer=answer3
elif choice == 4:
	answer=answer4
elif choice == 5:
	answer=answer5
#Print answer in selected number
print(answer)
