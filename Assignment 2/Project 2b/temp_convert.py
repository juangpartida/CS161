# Author: Juan Guillermo Partida
# Date: 01/08/24
# Description: This program will be converting a "Celsius" temperature input to a Fahrenheit
#              temperature. We were given the formula F = (9/5)C + 32


# Statement that tells the user to input a c temp
print("Please enter a Celsius temperature.")
# Actual input from end - user, which is -10.5 c
c = (float(input()))
# Formula to convert the inputted c Temp to f temp
f = ((c * 9.0 / 5.0) + 32.0)
# Statement that tells the user what the f temp is
print("The equivalent Fahrenheit temperature is:")
# Actual output of the converted f temperature
print(float(f))
