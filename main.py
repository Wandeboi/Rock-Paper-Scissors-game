import random

while True:
  
    print("R = rock")
    print("P = paper")
    print("S = scissors")
    user_action = input("Enter a choice (R, P, S): ")
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou ({user_action}), CPU ({computer_action}).\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
