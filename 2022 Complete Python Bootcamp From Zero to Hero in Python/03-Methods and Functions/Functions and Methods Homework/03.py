"""
Write a Python function that accepts a string
and calculates the number of upper case letters and lower case letters.
"""


def up_low(s):
    upper_case_char = 0
    lower_case_char = 0

    for char in s:
        if char.isupper():
            upper_case_char += 1
        elif char.islower():
            lower_case_char += 1
    print(f'No. of Upper case characters : {upper_case_char}')
    print(f'No. of Lower case Characters : {lower_case_char}')


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
