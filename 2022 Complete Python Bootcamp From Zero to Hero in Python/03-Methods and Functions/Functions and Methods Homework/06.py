"""
Write a Python function that checks whether a word or phrase is palindrome or not.

"""


def palindrome(s):
    reverse_str = s.replace(' ', '')[::-1]
    return reverse_str == s.replace(' ', '')


print(palindrome('helleh'))
print(palindrome('hello'))
print(palindrome('madam'))
print(palindrome('kayak'))
print(palindrome('racecar'))
print(palindrome('nurses run'))
