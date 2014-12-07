# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

__author__ = 'hannes'
import timeit
import math


def is_prime(p):  # check s whether p is prime
    return all(p % i for i in xrange(2, int(math.sqrt(p) + 1)))


def next_prime(p):  # return next prime number
    if p < 2:
        return 2
    while True:
        p += (1 if p % 2 == 0 else 2)
        if is_prime(p):
            return p


def prime_generator(n):  # n - number of primes to generate
    p = 0
    for x in range(0, n):
        p = next_prime(p)
    return p


print prime_generator(10001)
print timeit.Timer("prime_generator(10001)", setup="from __main__ import prime_generator").timeit(1)

# Congratulations, the answer you gave to problem 7 is correct. 104743 50.7462859154
# You are the 206222nd person to have solved this problem.