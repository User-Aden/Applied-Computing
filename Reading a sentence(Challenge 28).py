#Ask the user to enter a what sentence should have its vowels counted. - 05/05/25
d = str(input("What sentence would you like to count the amount of Vowels for: ")).lower()
#Start a counter to keep track of the number of vowels - 05/05/25
numberVowels = 0
#Loop checker through each letter in the sentence - 05/05/25
for letter in d:
    #Check if the letter is one of the vowels (a, e, i, o, u) - 05/05/25
    if letter in ("e", "a", "u", "o", "i"):
        #If it is a vowel, increase the counter by 1 - 05/05/25
        numberVowels += 1
#Prints the total number of vowels in the sentence is x amount' - 05/05/25
print("The number of vowels in the sentence is:", numberVowels)
