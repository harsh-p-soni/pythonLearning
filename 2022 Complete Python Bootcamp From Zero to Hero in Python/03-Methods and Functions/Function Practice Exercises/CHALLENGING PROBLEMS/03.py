"""
PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
out:   *
      * *
     *****
     *   *
     *   *
"""


def print_big(letter):
    my_new_dict = {0: '  *', 1: ' * * ', 2: '*****', 3: '*   *', 4: '*   *'}
    for item in range(0, 5):
        print(my_new_dict[item])


print_big('a')
