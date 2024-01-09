# Author: Juan Guillermo Partida
# Date: 01/09/24
# Description: This program will be a 2 user game (within the same terminal). The game will allow 1 end-user
#              to input an integer of their liking whilst the other tries to "guess" what the integer is.
#              If the 2nd user guesses too high, the game will notify them as so. If said user guesses too low
#              the game will notify them as well. The game will track how many guesses were attempted before
#              guessing correctly. Lastly, if said user guesses right on the first attempt, the game will
#              notify the user of this specific case with an alternate, specific, message.


# notifying user 1 for an integer input + identifying the variables with values.
print("Enter the integer for the player to guess.")
integer_num = int(input())
guess_attempt = 0

# notifying user 2 to beginning the "guess" integer inputs.
print("Enter your guess.")

# introduce a new variable within a while loop that will be used to track user 2's inputs
# while loop will be used to decide on 1 of 3 different "paths"
# is the integer too high? too low? or correct?

while True:
    guess_num = int(input())
    guess_attempt += 1
    if guess_num > integer_num:
        print("Too high - try again:")
        continue
    elif guess_num < integer_num:
        print("Too low - try again:")
        continue
    elif guess_attempt == 1:
        print("You guessed in 1 try.")
    else:
        break

# IF user 2 did not guess on 1 try, the program will use this output upon guessing right:
print("You guessed it in", guess_attempt, "tries.")


