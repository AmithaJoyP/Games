import random

def play_round():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in choices:
        print("Invalid choice! Try again.")
        return None, None
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        return "tie", computer_choice
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win", computer_choice
    else:
        return "lose", computer_choice

def rock_paper_scissors_best_of_3():
    user_score = 0
    computer_score = 0

    while user_score < 2 and computer_score < 2:
        result, computer_choice = play_round()
        if result == "win":
            user_score += 1
            print("You win this round!")
        elif result == "lose":
            computer_score += 1
            print("You lose this round!")
        else:
            print("This round is a tie!")
        
        print(f"Score - You: {user_score}, Computer: {computer_score}\n")

    if user_score == 2:
        print("Congratulations! You won the game!")
    else:
        print("Sorry, the computer won the game!")

if __name__ == "__main__":
    rock_paper_scissors_best_of_3()
