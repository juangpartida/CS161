# Author: Juan Guillermo Partida
# Date: 01/09/24
# Description: This program will output (print) a list of all the positive integers that may be
#              divided evenly based off of the end-user's initial positive integer input.
#              Please note, that this list will include the inputted positive integer itself and
#              and the number 1.


# get the positive integer input from the end-user
int_num = int(input("Please enter a positive integer:"))

# prints out the inputted positive integer to the end-user
print("The factors of", int_num, "are:")

# the letter "i" stands for the positive integer
# state the range between 1 and the initial positive integer
# initiate the for - if statement
for i in range(1, int_num + 1):
    if int_num % i == 0:
        # prints out the positive integers
        print(i)
