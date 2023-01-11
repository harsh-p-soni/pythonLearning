"""
COUNT PRIMES: Write a function that returns the number of prime numbers
that exist up to and including a given number
"""


def count_primes(num):
    my_prime_numbs = []
    for num in range(2, num + 1):
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            continue
        else:
            my_prime_numbs.append(num)
    print(len(my_prime_numbs))
    return my_prime_numbs


print(count_primes(100))
