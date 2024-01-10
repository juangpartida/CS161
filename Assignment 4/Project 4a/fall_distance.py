# Author: Juan Guillermo Partida
# Date: 01/10/24
# Description: Create a program that only contains the "Function Definition".
#              The function in itself, will determine the distance an object falls,
#              based off of the time period (in seconds) and gravity.

# formula that will be used: d = (1/2)gt^2
# g standing for gravity, d standing for distance, t standing for time

gravity = 9.8                                                                           # giving the variable a value


def fall_distance(time):                                                                # defining the "Function"
    dist = (1 / 2 * gravity * (time ** 2))
    """ returns the time in seconds, to be converted into distance """
    print(dist)
    return dist


# example of a giving the "Function" a defined value (value being in seconds)
# dist = fall_distance(3.2)
