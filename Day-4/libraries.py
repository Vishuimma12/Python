# Libraries in Python are a collection of modules that provide additional functionality.

# Commonly used libraries include:
import math  # Provides mathematical functions  and constants
import random  # Provides functions for generating random numbers 
import datetime  # Provides classes for manipulating dates and times
import os  # Provides functions for interacting with the operating system
import sys  # Provides access to system-specific parameters and functions
import json  # Provides functions for working with JSON data

# Example usage of the libraries
print("Welcome to the Libraries Example!")  

# fallow this documentation for more information: https://docs.python.org/3/library/

#  import --> it is used to include a module in your program

# Flpping a coin using the random library
print("\nFlipping a coin using the random library:")
import random #  # Importing the random library to use its functions
coin = random.choice(['Heads', 'Tails'])  # Randomly selects either 'Heads' or 'Tails' 
print(f"The coin landed on: {coin}")


from random import choice  # Importing only the choice function from the random library
coin2 = choice(['Heads', 'Tails'])  # Randomly selects either 'Heads' or 'Tails'
print(f"The coin landed on (using choice): {coin2}")  


print("\nGenerating a random number using the random library:")
random_number = random.randint(1, 100)  # Generates a random integer between 1 and 100
print(f"Random number between 1 and 100: {random_number}")  # Prints the generated random number


print("\n Shuffling a deck of cards using the random library:")
cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']  # List of cards
random.shuffle(cards)  # Shuffles the list of cards in place
print("Shuffled cards:")
for card in cards: 
    print(card)
    

print("\nCalculating mean, median, and mode using the statistics library:")
import statistics  # Importing the statistics library to use its functions

mean = statistics.mean([1, 2, 3, 4, 5])  # Calculates the mean of the list of numbers
print(f"\nMean of [1, 2, 3, 4, 5]: {mean}") 


median = statistics.median([1, 2, 3, 4, 5])  # Calculates the median of the list of numbers
print(f"Median of [1, 2, 3, 4, 5]: {median}")


mode = statistics.mode([1, 2, 2, 3, 4]) # Calculates the mode of the list of numbers
print(f"Mode of [1, 2, 2, 3, 4]: {mode}") 


import sys
print("\nUsing the sys library to get system information:")

if len(sys.argv) < 2:  # Check if the script is run with command line arguments
    sys.exit(" Too few arguments provided. Please provide your name as an argument.")
elif len(sys.argv) > 2:  # Check if more than one argument is provided
    print("Too many arguments provided. Please provide only your name as an argument.")

# for arg in sys.argv[1: -1]:  # Loop through the command line arguments
#     print("My name is:", arg)  # Print each argument passed to the script

print("Hello, My name is", sys.argv[1])  # Prints the name of the script being executed


# if we want to pass full name as an argument, we can use quotes in the command line
# Example: python libraries.py "John Doe"

