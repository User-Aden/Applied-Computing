import time
#Print the welcome to the challenge message - 05/05/25
print("Welcome to the say my name challenge.")
#Pause for 0.6 sec - 05/05/25
time.sleep(0.6)
#Ask the user for their first guess - 05/05/25
x = str(input("What is my first-name (3 Guesses): ")).capitalize()
#If the answer is Aden, print congratulations message - 05/05/25
if x == "Aden":
#Pause for 0.6 sec - 05/05/25
    time.sleep(0.6)
    print("Congratulations. You guessed my name in one guess!")
#If the answer is not Aden, print Nice try message - 05/05/25
else:
#Pause for 0.6 sec - 05/05/25
    time.sleep(0.6)
    d = str(input("Nice try but not quite. Take another guess (2 Guesses): ")).capitalize()
#If second guess is Aden print congratulations message - 05/05/25
    if d == "Aden":
#Pause for 0.6 sec - 05/05/25
        time.sleep(0.6)
        print("Congratulations. You guessed my name in two guesses!")
#If second guess is not Aden, print nice try message two - 05/05/25
    else:
#Pause for 0.6 sec - 05/05/25
        time.sleep(0.6)
        c = str(input("That's not it either. Don't worry, you have one more try! (1 Guess): ")).capitalize()
#If third answer is Aden, print congratulation message - 05/05/25
        if c == "Aden":
#Pause for 0.6 sec - 05/05/25
            time.sleep(0.6)
            print("Congratulations. You managed to guess my name!")
#If final guess is not Aden, print Sorry you're out of guesses - 05/05/25
        else:
#Pause for 0.6 sec - 05/05/25
            time.sleep(0.6)
            print("\n\nSorry, you're out of guesses. Better luck next time.")
