# Author: Juan Guillermo Partida
# Date: 01/8/2024
# Description: This program will ask the end user to provide 5 numbers and will print out the Average
#              of said numbers. The numbers inputted by end user are as described within the README
#              file. Method used for this assignment was drawn from Module 2, Exploration Input & Casting

print("Please enter five numbers.")
# end user will input -2.4
num_1 = float(input())
# end user will input  5.1
num_2 = float(input())
# end user will input  6.0
num_3 = float(input())
# end user will input 123.8
num_4 = float(input())
# end user will input -19.0
num_5 = float(input())
# will prompt end user what the average number is
print("The average of those numbers is:")
# finding the average of the inputted numbers above
avg = (num_1 + num_2 + num_3 + num_4 + num_5)/5.0
# printing the average found above
print(avg)
