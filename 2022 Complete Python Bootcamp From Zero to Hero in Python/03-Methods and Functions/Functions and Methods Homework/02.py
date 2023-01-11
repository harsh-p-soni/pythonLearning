"""
Write a function that checks whether a number is in a given range (inclusive of high and low)
"""


def ran_bool(num, low, high):
    return num > low and num < high


print(ran_bool(3, 1, 10))
print(ran_bool(5, 2, 7))
print(ran_bool(5, 1, 4))
