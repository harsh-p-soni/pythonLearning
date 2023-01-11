"""
Guessing Game Challenge
Let's use while loops to create a guessing game.

The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!
"""

from random import randint

my_random_number = randint(1, 101)
print('Guessing Game Challenge')
# print(f'Random number is {my_random_number}')
# my_random_number = 20

my_guesses = [0]

user_input = int(input('Guess your number: '))
my_guesses.append(user_input)
if user_input < 1 or user_input > 100:
    print('OUT OF BOUNDS')
else:
    if abs(user_input - my_random_number) > 10:
        print('COLD!')
    else:
        print('WARM!')

while my_random_number - my_guesses[-1]:
    user_input = int(input('Guess your number again: '))
    my_guesses.append(user_input)
    print(my_guesses)

    if my_guesses[-1] > my_guesses[-2]:
        print('WARMER!')
    else:
        print('COLDER')

number_of_guesses = (len(my_guesses) - 1)
print(f'You have correctly guess the number and took {number_of_guesses} attempts')







#print(abs(-5))















