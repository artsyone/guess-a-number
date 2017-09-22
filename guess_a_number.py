






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
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +".")
    print(" You will get " + str(limit) + "  tries. ")
    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

def show_result(guess, rand):
    if guess == rand:
         print( "Way to go. You can guess!")
    else:
         print( " Way to go, you suck the number was " + str(rand) + ".")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes' or decision == 'Y':
            return True
        elif decision == 'n' or decision == 'no' or decision == 'N':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

        print ("")

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
