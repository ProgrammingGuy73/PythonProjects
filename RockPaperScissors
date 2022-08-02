import random

print("ROCK, PAPER, SCISSORS GAME!")
print("Q to quit")

computer_wins = 0
player_wins = 0
draws = 0


def player_win_percentage():
    games = player_wins + computer_wins + draws
    value = player_wins / games
    return value * 100


while True:
    choices = ["rock", "paper", "scissors"]
    #            0        1         2
    random_number = random.randint(0, 2)
    computer_choice = choices[random_number]

    player_choice = input("> ").lower()

    if player_choice not in choices and player_choice != "q":
        print("You must choice either Rock, Paper or Scissors and nothing else!")
        continue
    elif player_choice == "q":
        break

    print(f"The computer picked: {computer_choice[0].upper()}{computer_choice[1:]}")

    if player_choice == computer_choice:
        print("It's a draw!")
        draws += 1
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You won!")
        player_wins += 1
    elif player_choice == "paper" and computer_choice == "rock":
        print("You won!")
        player_wins += 1
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You won!")
        player_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("THANKS FOR PLAYING!")
print(f"You won {player_wins} and computer won {computer_wins}")
print(f"Amount of draws: {draws}")
print(f"Your win percentage against the computer: {player_win_percentage()}%")
