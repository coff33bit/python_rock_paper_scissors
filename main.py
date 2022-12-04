import random

def get_play():
    player_choice = input("Enter choice: ")
    computer_options = ["paper", "rock", "scissors"]
    computer_choice = random.choice(computer_options)

    plays = {"Player": player_choice, "Computer": computer_choice}

    return plays

choices = get_play()

def check_win(player, computer):
    print(f"Player chose {player} and computer chose {computer}")
    if player == computer:
        return "Tie"
