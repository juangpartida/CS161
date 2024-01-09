# Author: Juan Guillermo Partida
# Date: 01/08/24
# Description: This program will prompt the end user to input an (integer) number of cents between
#              0 - 99. The outputs will be the fewest amounts of each coin in total ( Q, D, N, P).

# This statement will prompt the end user to input an (integer) number
print("Please enter an amount in cents less than a dollar.")
# input will be 87 Cents
cents = int(input())
# This statement will inform the end user of the output of 87 cents broken down into smaller sets of coins
print("Your change will be:")
# Applying the Floor Division which rounds down to the nearest whole number
print("Q:", cents // 25)
# Applying the Modulus Operator  which gives us the remainder of the left to the right operand
cents = cents % 25
# Applying the Floor Division Operator which rounds down to the nearest whole number
print("D:", cents // 10)
cents = cents % 10
# Applying the Floor Division Operator which rounds down to the nearest whole number
print("N:",  cents // 5)
# Applying the Modulus Operator  which gives us the remainder of the left to the right operand
cents = cents % 5
# Simple print of "P" ie Pennies pulled from Cents as there's no conversion needed
print("P:",  cents)
