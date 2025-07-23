import random
keep_playing = "Y"

while keep_playing == "Y":
    number = random.randint(1,20)
    guess = -1
    guess_count = 0

    while guess != number:
        guess = int(input("Guess a number between 1 and 20: "))
        guess_count = guess_count + 1
        if guess < number:
            print("Too low! Try again!")
        elif guess > number:
            print("Too high! Try again!")
        else:
            print("Congratulations, you guessed it!")
            print(f"I took you {guess_count} guesses to guess the number!")

    keep_playing = input("Do you want to try again? (Y/N)")
    