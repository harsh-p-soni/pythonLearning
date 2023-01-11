"""
Write a Python function to multiply all the numbers in a list.
"""


def multiply(numbers):
    mul = 1
    for num in numbers:
        mul = mul * num

    return mul


print(multiply([1, 2, 3, -4]))

