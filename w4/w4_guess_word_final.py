secret_word = "mosiah"
guess_count = 0

print("Welcome to the word guessing game!")

while True:
    guess_count += 1

    initial_hint = "_ " * len(secret_word)
    print(f"\nYour hint is: {initial_hint.strip()}")

    user_guess = input("What is your guess? ").lower()

    if len(user_guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue

    if user_guess == secret_word:
        print("\nCongratulations! You guessed it!")
        print(f"It took you {guess_count} guesses.")
        break
    else:
        current_hint_list = ["_"] * len(secret_word)

        for i in range(len(secret_word)):
            secret_char = secret_word[i]
            guess_char = user_guess[i]

            if guess_char == secret_char:
                current_hint_list[i] = guess_char.upper()
            elif guess_char in secret_word:
                current_hint_list[i] = guess_char.lower()
            
        hint_display = " ".join(current_hint_list)
        print(f"Your hint is: {hint_display}")