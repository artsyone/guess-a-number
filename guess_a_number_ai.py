
import time
import random

# config
import math
tries = 1 

# helper functions

def show_start_screen():
    
    print("""   ______                        ___       _   __                __             
  / ____/_  _____  __________   /   |     / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/  / /| |    /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )  / ___ |   / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/  /_/  |_|  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/     
                                                                                """)
    print("") 

def show_credits():
    print("""       ______                        ____                 
      / ____/___ _____ ___  ___     / __ \_   _____  _____
     / / __/ __ `/ __ `__ \/ _ \   / / / / | / / _ \/ ___/
    / /_/ / /_/ / / / / / /  __/  / /_/ /| |/ /  __/ /    
    \____/\__,_/_/ /_/ /_/\___/   \____/ |___/\___/_/ """)

    
    print("This awesome game was created by Savanna S.")
    print(" That was fun! Bye " + str(name) + "." )
    

def ask_name():
    
    print ("Before we start I would like to know who im playing against ")
    print("Type your name")
    name = input ()

    return name

def pick_low():
        print("Please enter the numbers we will play between " + str(name) + ".")
        print(" Enter the low ")
        low = input()

        return int(low) 
       
def pick_high ():
        print ("Enter the high ")
        high = input ()

        return int(high)
    
def get_guess(current_low, current_high):
    """
    Returns a truncated average of the current low and high
    """
    guess = (current_high + current_low )//2
    
   
    return guess 

def pick_number(current_low,current_high,name):
    """    Ask the player to pick a number and waits until the player
    confirms they have a number by pressing enter.
    """
    
    
    print( " Think of a number from " +  str(current_low) + " to " + str(current_high) + " . Im going to try to guess it." )
    print("")
    print(" I will get " + str(limit) + " tries, to guess your number. ")
    print ("   ")
    time.sleep(1)
    print("Press enter to contine " + str(name) + ".")
    print ("   ")
    input ()
    
def check_guess(guess):
    """
    Ask the player if the computer's number was too high, too low,
    or just right.
    
    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    
    while True:
        print("")
        print (" Is your number " + str(guess) + "." )
        print ("   ")
        time.sleep(1) 

        print(" Guess " + str(tries) + " of " + str(limit)+ ".")
        decision = input(" Please input whether the number your thinking of is ...(lower / higher / yes)")
        print("")

        
        decision = decision.lower()
        if decision == 'low' or decision == 'lower'or decision == 'l':
            return 1
        elif decision == 'high' or decision == 'higher'or decision == 'h':
            return -1
        elif decision == 'yes'or decision == 'yes'or decision == 'yeah' or decision == 'y':
            return 0

        else:
            print(" **** I dont understand " + str(name)+ " please print h,l or y. ***** ")

def show_result():
    print("Haha I got it.")
    print("")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        
        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand " + str(name) + " . Please enter 'y' or 'n'.")

def play(name):

    current_low = pick_low()
    current_high = pick_high()
    
    global tries 
    tries = 1 
       
    result = -1

    global limit 
    limit = math.ceil(math.log( current_high - current_low + 1 ,2))
    
    pick_number (current_low,current_high,name)

    while result != 0:
        guess = get_guess(current_low, current_high)
        result = check_guess(guess)
    
            
        if result == -1 :         
            current_low = guess + 1 
            tries += 1 
        elif result == 1 :
            current_high = guess - 1
            tries += 1
    
    show_result()

# Game starts running here
show_start_screen()
name = ask_name()
playing = True

while playing:
    play(name)
    
    playing = play_again()
    

show_credits()
