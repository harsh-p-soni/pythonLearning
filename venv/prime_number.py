prime_number_list = []
for number in range(1, 101):
    if number == 1:
        print("It's not a prime number.")
    elif number == 2 or number == 3 or number == 5 or number == 7:
        prime_number_list.append(number)
        print("It's a prime number.")
    elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        print("It's not a prime number.")
    else:
        prime_number_list.append(number)
        print("It's a prime number.")

print(prime_number_list)

