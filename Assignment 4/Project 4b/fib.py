# Author: Juan Guillermo Partida
# Date: 01/10/24
# Description: Create a program that only contains the a defined Function.
#              This function will take a positive integer with a parameter
#              that will return said number (integer) at its given position
#              using the "Fibonacci"  Sequence.


# defining the "Function"
def fib(input_num):

    # giving the variables a value
    num_1 = 1
    num_2 = 1
    # initiate the if, elif, else statements to cover the end user number inputs

    if input_num == 1:
        # cover the sum of the two first numbers of the Fib Sequence, which returns the total sum, being 1
        return 1

    elif input_num == 2:
        # cover the sum of the two first numbers of the Fib Sequence, which returns the total sum, being 1
        return 1
    else:
        # initiate the while loop to cover the positive integers that has a sum greater than 2 using the Fib Sequence
        while input_num > 2:
            num_3 = num_1 + num_2
            num_1 = num_2
            num_2 = num_3
            input_num = input_num - 1
        """ will return the sum of each subsequent number after the two first positive integers 
            each subsequent number is the sum of the two preceding numbers
        """
        return num_3

# user testing: term = fib(insert positive integer here) then proceed to print term
# term = fib(1)
# term = fib(10)
# term = fib(17)
# print(term)
