word = "mosiah"
count = 0
guess = ""

while word != guess:
    count = count + 1
    guess = input("What is your guess?\n")

print(f"It took you {count} guesses to guess the word.")
   

