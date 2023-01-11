def create_cube(n):
    for x in range(n):
        yield x ** 3
    print('End of func for loop')


for x in create_cube(10):
    print('Start of for loop')
    print(x)
