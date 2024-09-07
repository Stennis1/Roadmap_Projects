#A number guessing game with three levels of difficulty 

#import modules 
import random
import sys
import time 

#Display rules and clues of the game 
def display_welcome_message():            
    print(
        """Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
Press 'q' to quit"""
        )            


def get_difficulty_level():
    #Options to quit the game 
    options = ["q", "quit", "exit", "exit()", "logout"]

    while True:
        #Accept user prompt to begin game
        user_input = input("Enter your choice: ")
        
        if user_input == "1":
                print("Great! You have selected the Easy difficulty level. Let's start the game!")
                return 10
            
        elif user_input == "2":
                print("Great! You have selected the Medium difficulty level. Let's start the game!")
                return 5
            
        elif user_input =="3":
                print("Great! You have selected the Esay difficulty level. Let's start the game!")
                return 3
            
        elif user_input in options:
                print("Goodbye! Come back soon.")
            
        else:
            print("Please enter a valid number. (1, 2, 3 or 'q' to quit).")


def play_game():
    chances = get_difficulty_level()
    computer_pick = random.randint(1,101)
    user_attempts = 0
    start_time = time.time()
    
    while user_attempts < chances:
        try:
            user_pick = int(input("Enter your guess: "))
            user_attempts += 1

            if user_pick == computer_pick:
                end_time = time.time()
                time_taken = round(end_time - start_time, 2)
                print(f"Congratulations! You guessed the number in {user_attempts} attempts and took {time_taken} seconds.")
                return user_attempts
                            
            elif user_pick < computer_pick:
                print("Incorrect! Your guess is less than the number.")
                
            else:
                print("Incorrect! Your guess is greater is greater than the number.") 

        except ValueError:
            print("Please enter a valid number.")
    
    print(f"Sorry, you have run out of chances. The correct number was {computer_pick}")
    return user_attempts


def play_again():
    while True:
        again = input("Do you want to play again(y/n): ").lower()
        
        if again == "y":
            return True
        
        elif again == "n":
            return False
        
        else:
            print("Invalid input, please enter 'y' or 'n'.")


def number_guessing_game():
        
    user_high_score = float('inf')

    while True:
        display_welcome_message()
        user_attempts = play_game()

        if user_attempts < user_high_score:
             user_high_score = user_attempts
             print(f"New High score: {user_high_score}")

        if not play_again():
             print("Thank you for playing! Goodbye.")
             break 


#Run the game 
number_guessing_game()

sys.exit()

