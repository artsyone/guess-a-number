






import random

# config
import math

low = 1
high = 100
limit = math.ceil (math.log( high - low + 1 ,2))

# helper functions




def show_start_screen():
    
    print("""   ______                        ___       _   __                __             
  / ____/_  _____  __________   /   |     / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/  / /| |    /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )  / ___ |   / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/  /_/  |_|  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/     
                                                                                """)
  

def show_credits():
    print("""       ______                        ____                 
      / ____/___ _____ ___  ___     / __ \_   _____  _____
     / / __/ __ `/ __ `__ \/ _ \   / / / / | / / _ \/ ___/
    / /_/ / /_/ / / / / / /  __/  / /_/ /| |/ /  __/ /    
    \____/\__,_/_/ /_/ /_/\___/   \____/ |___/\___/_/ """)

    
    print("This awesome game was created by Sav Shav.")
    
def get_guess(current_low, current_high):
    """
    Returns a truncated average of the current low and high
    """
    pass

def pick_number():
    """
    Ask the player to pick a number and waits until the player
    confirms they have a number by pressing enter.
    """
    pass

def check_guess(guess):
    """
    Ask the player if the computer's number was too high, too low,
    or just right.
    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    pass

def show_result():
    pass

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    result = -1
    
    pick_number()
    
    while result != 0:
        guess = get_guess(current_low, current_high)

        result = check_guess(guess)

        if result == -1:
            # adjust current high
            pass
        elif result == 1:
            # adjust current low
            pass

    show_result()

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
