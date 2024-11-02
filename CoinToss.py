import random

def coin_toss():
    print("Welcome to the Coin Toss Game!")
    user_guess = input("Guess 'heads' or 'tails': ").lower()
    if user_guess not in ["heads", "tails"]:
        print("Invalid guess! Please choose 'heads' or 'tails'.")
        return
    
    toss_result = random.choice(["heads", "tails"])
    print(f"The coin landed on: {toss_result}")
    
    if user_guess == toss_result:
        print("Congratulations! You guessed it right!")
    else:
        print("Sorry, better luck next time!")

if __name__ == "__main__":
    coin_toss()
