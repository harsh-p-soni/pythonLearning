"""
Errors and Exceptions Homework
Problem 1
Handle the exception thrown by the code below by using try and except blocks.
"""

try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print('Incorrect input provided')


"""
Problem 2
Handle the exception thrown by the code below by using try and except blocks. 
Then use a finally block to print 'All Done.'
"""

try:
    x = 5
    y = 0

    z = x / y
except ZeroDivisionError:
    print('Division by 0 is not allowed')
finally:
    print('All Done')


"""
Problem 3
Write a function that asks for an integer and prints the square of it. 
Use a while loop with a try, except, else block to account for incorrect inputs.
"""


def ask():
    while True:
        try:
            my_int = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
        else:
            print(f"Thank you, your number squared is: {my_int ** 2}")
            break



ask()