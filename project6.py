# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + 3**2 + 4**2 ...
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)**2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
__author__ = 'hannes'
import timeit


def sum_of_squares(n):
    return sum(map(lambda x: x ** 2, range(1, n + 1)))


def square_of_sum(n):
    return sum(range(1, n + 1)) ** 2


def delta(n):
    return square_of_sum(n) - sum_of_squares(n)


print timeit.Timer("delta(100)", setup="from __main__ import delta").timeit(1)
print delta(100)

# Congratulations, the answer you gave to problem 6 is correct.
# You are the 240524th person to have solved this problem.