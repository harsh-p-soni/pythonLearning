"""
PAPER DOLL: Given a string, return a string where for every character in the original
there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
"""


def paper_doll(text):
    new_str = ''
    for letter in text:
        new_str = new_str + letter * 3

    return new_str


print(paper_doll('Hello'))

print(paper_doll('Mississippi'))

