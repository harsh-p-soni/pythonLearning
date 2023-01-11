"""
Write a Python function to check whether a string is pangram or not.
(Assume the string passed in does not have any punctuation)
"""


import string


def ispangram(str1, alphabet=string.ascii_lowercase):

    my_new_set = set(str1.lower().replace(' ', ''))
    my_alphabet_set = set(alphabet)

    return my_alphabet_set.difference(my_new_set) == 0


print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("It is really cold in the morning for ahmendabad people working really good for longer times in a company"))

