#Ask the user which team they belong to, and put response into capital letters - 03/05/25
choice = input("Which home group are you in: ").upper()
#If user's answer is a B or K team homegroup, then print special offer - 03/05/25
if choice in ("XB1", "XB2", "XB3", "XB4", "XK1", "XK2", "XK3", "XK4"):
    print("We have a special offer of 10% off ferrets for students in B or K team")
#If user input is not specified options, print Sorry you have not made a valid choice - 03/05/25
elif choice not in ("XB1", "XB2", "XB3", "XB4", "XK1", "XK2", "XK3", "XK4"):
    print("Sorry you have not made a valid choice")
