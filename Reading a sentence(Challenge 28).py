# Ask the user to enter a what sentence should have it's vowels counted.
d = str(input("What sentence would you like to count the amount of Vowels for: ")).lower()
#Start a counter to keep track of the number of vowels
numberVowels = 0
#Loop checker through each letter in the sentence
for letter in d:
#Check if the letter is one of the vowels (a, e, i, o, u)
    if letter in ("e", "a", "u", "o", "i"):
#If it is a vowel, increase the counter by 1
        numberVowels += 1
#Print 'The total number of vowels in the sentence is x amount
print("The number of vowels in the sentence is:", numberVowels)
