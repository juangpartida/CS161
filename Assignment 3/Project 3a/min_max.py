# Author: Juan Guillermo Partida
# Date: 01/09/24
# Description: This program will ask the end user how many integers they would like to enter.
#              No matter how the end user inputs the integers, the program will output the
#              smallest AND largest integers.

# Prompts user on what to do & notifies user of inputted number of integers
# includes an end-user input function to be used for the later print immediately after

print("How many integers would you like to enter?")
num_1 = int(input())
print("Please enter", num_1, "integers.")

# creating variables for Min and Max

minimum_Value = int(input())
maximum_Value = minimum_Value

# using the letter "i" and "n" as variables for integers and numbers (inputted) respectively.
# initiating a "for" loop with a "range" embedded in the statement to capture the inputted numbers.
# implement the "if" statements for MAX and MIN that will later be used for the print function.

for i in range(1, num_1):
    n = int(input())
    if n > maximum_Value:
        maximum_Value = n
    if n < minimum_Value:
        minimum_Value = n

# end-user's output
print("min:", minimum_Value)
print("max:", maximum_Value)
