import random

def get_choices():
    player_choice = input("Enter choice: ")
    computer_options = ["paper", "rock", "scissors"]
    computer_choice = random.choice(computer_options)

    plays = {"Player": player_choice, "Computer": computer_choice}

    return plays

def check_win(player, computer):
    print(f"Player chose {player} and computer chose {computer}")
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "paper":
            return "paper covers rock, computer wins!"
        else:
            return "rock breaks scissors, player wins!"
    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper, player wins"
        else:
            return "rock breaks scissors, computer wins"
    elif player == "paper":
        if computer == "scissors":
            return "scissors cuts paper, computer wins"
        else:
            return "paper covers rock, player wins"
    else:
        return "invalid choice, no winner"


choices = get_choices()

result = check_win(choices["Player"], choices["Computer"])

print(result)