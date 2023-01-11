"""
This exercise will require several lines of code.

Write a script that opens a file named 'test.txt' , writes 'Hello World'  to the file, then closes it.

"""

myFile = open('test.txt', 'w')
myFile.write('Hello World')
myFile.close()

# Using with
# with open('test.txt', mode='w+') as f:
#     f.write('This is is my first line')
#     print(f.read())
#     f.close()
