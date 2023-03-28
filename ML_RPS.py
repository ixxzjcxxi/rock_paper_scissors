import random

print("Welcome to Rock, Paper, Scissors!")
user_name = input("What's your name? ")

print(f"\nWelcome {user_name}, let's play Rock, Paper, Scissors. Best 2 out of 3 wins! Let's see if you can beat me!")
print("\nHere is how this works: I'll ask you what you want (Rock, Paper, Scissors), then the computer will randomly pick one. Whoever wins gets a point added. Whoever wins twice wins the game!")


def game_play(difficulty):
    choices = ["Rock", "Paper", "Scissors"]
    play_again = "Y"
    while play_again == "Y":
        user_wins = 0
        computer_wins = 0
        previous_choices = []
        while user_wins < 2 and computer_wins < 2:
            if difficulty == "easy":
                computer_pick = random.choice(choices)
            elif difficulty == "medium":
                # generate computer's pick based on user's previous choices
                # if user has not made any previous choices, pick randomly
                if len(previous_choices) == 0:
                    computer_pick = random.choice(choices)
                else:
                    # count how many times each choice appears in previous_choices
                    choice_counts = [previous_choices.count(choice) for choice in choices]
                    # pick the choice with the lowest count (i.e. the least common choice)
                    computer_pick = choices[choice_counts.index(min(choice_counts))]
            else:
                # generate computer's pick based on a simple AI algorithm
                # this algorithm assumes that the user will not pick the same choice twice in a row
                if len(previous_choices) == 0:
                    computer_pick = random.choice(choices)
                else:
                    last_choice = previous_choices[-1]
                    # determine which choices would beat the user's last choice
                    if last_choice == choices[0]:
                        computer_pick = choices[1]
                    elif last_choice == choices[1]:
                        computer_pick = choices[2]
                    else:
                        computer_pick = choices[0]
            
            user_choice = input(f"\nOkay {user_name}, what do you want:\n1)Rock\n2)Paper\n3)Scissors\nYour Choice: ")
            if user_choice not in "123":
                print("Sorry, I don't understand that. Please pick a number 1-3.")
                continue
            if user_choice == "1" or user_choice.lower() == "rock":
                user_choice = choices[0]
            elif user_choice == "2" or user_choice.lower() == "paper":
                user_choice = choices[1]
            else:
                user_choice = choices[2]

            if user_choice == choices[0] and computer_pick == choices[2]:
                print(f"\nYou win! You picked {user_choice} and computer picked {computer_pick}")
                user_wins += 1
            elif user_choice == choices[1] and computer_pick == choices[0]:
                print(f"\nYou win! You picked {user_choice} and computer picked {computer_pick}")
                user_wins += 1
            elif user_choice == choices[2] and computer_pick == choices[1]:
                print(f"\nYou win! You picked {user_choice} and computer picked {computer_pick}")
                user_wins += 1
            elif user_choice == computer_pick:
                print(f"\nIt's a tie! You picked {user_choice} and computer picked {computer_pick}")
            else:
                print(f"\nYou lose! You picked {user_choice} and computer picked {computer_pick}")
                computer_wins += 1
            print(f"Computer wins:{computer_wins}\nUser Wins:{user_wins}")

        if user_wins > computer_wins:
            print(
                f"\nNice Game! You won {user_wins}, and computer won {computer_wins}")
        else:
            print(
                f"You tried your best,  you  won {user_wins}, computer won {computer_wins}")
        play_again = input("Do you want to play again? Y/N: ")
        if play_again.upper() == "Y":
            print("Awesome get ready to play!!")
            play_again = "Y"
            continue
        else:
            print("Play again SOOOOOON!")
            break


game_play()
