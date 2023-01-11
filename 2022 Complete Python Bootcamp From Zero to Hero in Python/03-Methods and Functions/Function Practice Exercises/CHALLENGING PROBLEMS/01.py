"""
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
"""


def spy_game(nums):
    my_new_str = ''
    for num in nums:
        if num == 0 or num == 7:
            my_new_str = my_new_str + str(num)
    if my_new_str == '007':
        return True
    else:
        return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))
