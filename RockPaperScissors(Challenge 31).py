import time
import random
# Ask the user for number of rounds they want to play - 6/05/25
x = int(input("How many rounds of R.P.S would you like to play (3-10): "))
# Check if the input is outside the valid range - 6/05/25
if x < 3 or x > 10:
#Pause for 0.5 seconds - 6/05/25
    time.sleep(0.5)
    print("I'm sorry, you can can only play matches in numbers of 3 - 10")
else:
#Pause for 0.5 seconds - 6/05/25
    time.sleep(0.5)
#Print the game starting message - 6/05/25
    print("Ok, let's play!")
#Pause for 0.5 seconds - 6/05/25
    time.sleep(0.5)
#Start the player's score as 0 - 6/05/25
    player_score = 0
#Start the computer's score as 0 - 6/05/25
    computer_score = 0
#Round counter, this helps count how many rounds there are - 6/05/25
    for round_number in range(1, x + 1):
#Pause for 0.5 seconds - 6/05/25
        time.sleep(0.5)
#Print the current round number - 6/05/25
        print(f"\nRound {round_number}:")
#Get the player's input - 6/05/25
        playa = input("Rock, Paper, or Scissors (Careful not to mistype): ").capitalize()
#List of computers possible moves - 6/05/25
        choices = ["Rock", "Paper", "Scissors"]
#Computer picks one of the the three options - 6/05/25
        computer_choice = random.choice(choices)
#Pause for 0.5 seconds - 6/05/25
        time.sleep(0.5)
#Print both player's and computer's choice - 6/05/25
        print("Player: " + playa + " v.s Computer: " + computer_choice)
#If both of them choose same, it's a draw - 6/05/25
        if playa == computer_choice:
            print("It's a draw!")
#How each of the moves interact with each other - 6/05/25
        elif (playa == "Rock" and computer_choice == "Scissors") or \
             (playa == "Paper" and computer_choice == "Rock") or \
             (playa == "Scissors" and computer_choice == "Paper"):
#Pause for 0.5 seconds - 6/05/25
            time.sleep(0.5)
#If the player wins the round, print this - 6/05/25
            print("You win this round!")
            player_score += 1
        else:
#Pause for 0.5 seconds - 6/05/25
            time.sleep(0.5)
#If the computer wins the round, print this - 6/05/25
            print("The Computer wins this round!")
            computer_score += 1
#Pause for 0.5 seconds - 6/05/25
    time.sleep(0.5)
#After all rounds have been played, print Game over - 6/05/25
    print("\n\nGame Over!")
#Pause for 0.5 seconds - 6/05/25
    time.sleep(0.5)
#Show the player's final score - 6/05/25
    print("Player score:", player_score)
#Show the computer's final score - 6/05/25
    print("Computer score:", computer_score)
#If player has more points - 6/05/25
    if player_score > computer_score:
# Print the player wins this match - 6/05/25
        print("\n\nYou Win This Match Of R.P.S!")
#If Computer has more points - 6/05/25
    else:
#Print You lose this match - 6/05/25
        print("\n\nYou Lose This Match of R.P.S, Better Luck Next-Time.")
