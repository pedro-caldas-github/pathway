number = 10

guess = -1

while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        print("Too low! Try again!")
    elif guess > number:
        print("Too high! Try again!")
    else:
        print("Congratulations, you guessed it!")
    print("Do you want to try again? (yes/no)")
    