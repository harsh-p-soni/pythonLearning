"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald
"""


def old_macdonald(name):
    new_str_1 = ''
    x = 1
    for letter in name:
        if x == 1:
            new_str_1 = new_str_1 + letter.capitalize()
        elif x == 4:
            new_str_1 = new_str_1 + letter.capitalize()
        else:
            new_str_1 = new_str_1 + letter
        x = x + 1

    return new_str_1


print(old_macdonald('macdonald'))

print(old_macdonald('hello'))


