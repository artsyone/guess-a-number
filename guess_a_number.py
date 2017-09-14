
#config

import random
low = 1
high = 100
limit = 10

rand = random.randint(low,high)
print("I'm thinking of a number from " + str(low) + " to " + str(high)+ ".");

# start game 
guess = -1
tries=0

# play game 
while guess != rand and tries < limit:
    guess = input("Take a guess: ")
    guess = int(guess)
    
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
