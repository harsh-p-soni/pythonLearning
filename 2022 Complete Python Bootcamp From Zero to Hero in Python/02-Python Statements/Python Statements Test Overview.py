"""

 ___

Content Copyright by Pierian Data
Statements Assessment Test
Let's test your knowledge!

Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
#Code here
Use range() to print all the even numbers from 0 to 10.

#Code Here
Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

#Code in this cell
[]
Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
#Code in this cell
Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

#Code in this cell
Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
#Code in this cell
Great Job!
"""

st = 'Print only the words that start with s in this sentence'
for word in st.split(' '):
    if word[0] == 's':
        print(word)

for num in range(0, 11):
    if num % 2 == 0:
        print(num)

my_list = [num for num in range(0, 51) if num % 3 == 0]
print(my_list)

st = 'Print every word in this sentence that has an even number of letters'
for item in st.split(' '):
    if len(item) % 2 == 0:
        print('even')


for num in range(0, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    else:
        if num % 3 == 0:
            print('Fizz')
        elif num & 5 == 0:
            print('Buzz')

st = 'Create a list of the first letters of every word in this string'
new_st = [letter[0] for letter in st.split(' ')]
print(new_st)

