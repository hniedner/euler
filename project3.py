# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
__author__ = 'hannes'
# thanks to http://stackoverflow.com/questions/15347174/python-finding-prime-factors

# Wikipedia
# A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# A simple but slow method of verifying the primality of a given number n is known as trial division.
# It consists of testing whether n is a multiple of any integer between 2 and sqrt{n}.
import timeit


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


print(max(prime_factors(600851475143)))
print timeit.Timer("prime_factors(600851475143)", setup="from __main__ import prime_factors").timeit(1)

# Congratulations, the answer you gave to problem 3 is correct.
# You are the 248768th person to have solved this problem.