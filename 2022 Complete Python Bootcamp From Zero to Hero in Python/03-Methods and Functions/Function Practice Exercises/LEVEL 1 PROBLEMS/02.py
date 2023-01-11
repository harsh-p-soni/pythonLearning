"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
"""


def master_yoda(text):
    my_split_list = text.split(' ')
    my_reverse_list = []

    for i in range(1, (len(my_split_list) + 1)):
        my_reverse_list.append(my_split_list[-i])

    return my_reverse_list


print(master_yoda('I am home'))

print(master_yoda('We are ready'))

print(master_yoda('How are you my brother'))
