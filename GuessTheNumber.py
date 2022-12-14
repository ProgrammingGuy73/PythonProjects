import random

print("GUESS THE RANDOM NUMBER! FROM 1-9")
random_number = random.randint(1, 9)

wrong_counter = 0
while True:
    if wrong_counter == 3:
        print("You have used up all 3 guesses!")
        break

    print("GUESS A NUMBER: ")
    guess = input("> ")

    if len(guess) > 1 and guess.isdigit():
        print("You must guess 1 number at a time!")
        quit()
    elif not guess.isdigit():
        print("YOU MUST GUESS A NUMBER! NOT A LETTER!")
        quit()
    elif int(guess) == random_number:
        print("You guessed it!")
        break
    else:
        print("YOU GUESSED WRONG!")
        wrong_counter += 1
        continue

print(f"The secret number is {random_number}!")
print("THANKS FOR PLAYING!")

