
#config

import random
low = 1
high = 100
limit = 10

rand = random.randint(low,high)
print("I'm thinking of a number from " + str(low) + "  to " + str(high)+ ".");

#helper fuctions
def get_guess():
    while True:
        guess = input ("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")
        
# start game
rand = random.randint(low,high)
print("Im thinking of a number from" +str(low) + " to " + str(high) +". You have" + str(limit) + "tries to guess it.")

guess = -1
tries=0

# play game 
while guess != rand and tries < limit:
    guess = get_guess()
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")
    else:
        print("You got it!")

    tries += 1

#game end
if guess == rand:
    print( "Way to go. You can guess!")
else:
    print( " Way to go, you suck the number was " + str(rand) + ".")
