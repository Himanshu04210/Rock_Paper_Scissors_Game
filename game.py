import random

def get_user_choice():
    valid_choices = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice == 'quit':
            return user_choice
        if user_choice in valid_choices:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return 'user'
    else:
        return 'computer'

def play_game():
    user_wins = 0
    computer_wins = 0
    draws = 0
    while True:
        print("\n--- New Round ---")
        user_choice = get_user_choice()
        if user_choice == 'quit':
            break
        computer_choice = get_computer_choice()
        print("Computer chose:", computer_choice)
        winner = determine_winner(user_choice, computer_choice)
        if winner == 'user':
            print("You win!")
            user_wins += 1
        elif winner == 'computer':
            print("Computer wins!")
            computer_wins += 1
        else:
            print("It's a draw!")
            draws += 1
        print("Score: User -", user_wins, "\n Computer -", computer_wins, "\n Draws -", draws)

play_game()
