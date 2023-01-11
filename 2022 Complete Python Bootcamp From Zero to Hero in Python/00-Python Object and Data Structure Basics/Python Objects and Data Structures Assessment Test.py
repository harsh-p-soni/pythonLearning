"""

 ___

Content Copyright by Pierian Data # Objects and Data Structures Assessment Test
Test your knowledge.
** Answer the following questions **

Write (or just say out loud to yourself) a brief description of all the following Object Types and Data Structures we've learned about. You can edit the cell below by double clicking on it. Really this is just to test if you know the difference between these, so feel free to just think about it, since your answers are self-graded.

Double Click HERE to edit this markdown cell and write answers.

Numbers:

Strings:

Lists:

Tuples:

Dictionaries:

Numbers
Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25


Answer these 3 questions without typing code. Then type code to check your answer.

What is the value of the expression 4 * (6 + 5)

What is the value of the expression 4 * 6 + 5

What is the value of the expression 4 + 6 * 5

What is the type of the result of the expression 3 + 1.5 + 4?


What would you use to find a number’s square root, as well as its square?

# Square root:
# Square:
Strings
Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

s = 'hello'
# Print out 'e' using indexing
Reverse the string 'hello' using slicing:

s ='hello'
# Reverse the string using slicing
Given the string hello, give two methods of producing the letter 'o' using indexing.

s ='hello'
# Print out the 'o'

# Method 1:
# Method 2:
Lists
Build this list [0,0,0] two separate ways.

# Method 1:
# Method 2:
Reassign 'hello' in this nested list to say 'goodbye' instead:

list3 = [1,2,[3,4,'hello']]
Sort the list below:

list4 = [5,3,4,6,1]
Dictionaries
Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}
# Grab 'hello'
d = {'k1':{'k2':'hello'}}
# Grab 'hello'
# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello
# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
Can you sort a dictionary? Why or why not?


Tuples
What is the major difference between tuples and lists?


How do you create a tuple?


Sets
What is unique about a set?


Use a set to find the unique values of the list below:

list5 = [1,2,2,33,4,4,11,22,3,3,2]
Booleans
For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.

Operator	Description	Example
==	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
!=	If values of two operands are not equal, then condition becomes true.	(a != b) is true.
>	If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
<	If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
>=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b) is not true.
<=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	(a <= b) is true.
What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# Answer before running cell
2 > 3
# Answer before running cell
3 <= 2
# Answer before running cell
3 == 2.0
# Answer before running cell
3.0 == 3
# Answer before running cell
4**0.5 != 2
Final Question: What is the boolean output of the cell block below?

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']
Great Job on your first assessment!
"""

# Numbers
print(500 / 5 * 2 ** 2 + 0.50 - 300.25)
print(4 * (6 + 5))
print(4 * 6 + 5)
print(4 + 6 * 5)
print(type(3 + 1.5 + 4))
s = 'hello'
print(s[1])
print(s[0:5:1])
print(s[-1:-6:-1])
print(s[-1])
print(s[0:5:4][1])

new_letter = [0, 0]
new_letter.append(0)
print(new_letter)

my_new_list = [0]
my_second_list = [0, 0]
my_third_list = my_new_list + my_second_list
print(my_third_list)

list3 = [1, 2, [3, 4, 'hello']]
list3[2][2] = 'Goodbye'
print(list3)


list4 = [5, 3, 4, 6, 1]
list4.sort()
print(list4)

d = {'simple_key': 'hello'}
print(d['simple_key'])

d = {'k1': {'k2': 'hello'}}
print(d['k1']['k2'])

d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]

my_set = {1, 2, 2, 33, 4, 4, 11, 22, 3, 3,2}
print(my_set)

print(2 > 3)
print(3 <= 2)
print(3 == 2.0)
print(3 == 3.0)
print(4**0.5 != 2)

l_one = [1, 2, [3, 4]]
l_two = [1, 2, {'k1': 4}]
print(l_one[2][0] >= l_two[2]['k1'])
