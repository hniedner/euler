# Find the sum of all the multiples of 3 or 5 below 1000.
__author__ = 'hniedner@gmail.com'

import timeit


def calc_total(i, j):
    total = 0
    for x in range(i, j):
        if (x % 3 == 0) or (x % 5 == 0):
            total += x
    return total


print timeit.Timer("calc_total(0, 1000)", setup="from __main__ import calc_total").timeit(1)

# Congratulations, the answer you gave to problem 1 is correct.
# You are the 414618th person to have solved this problem.

# update with filter and reduce


def _add(t, a):
    return t + a


def _filter(a):
    return (a % 3 == 0) or (a % 5 == 0)


def calc_total_improved(i, j):
    return reduce(_add, filter(_filter, range(i, j)))


print timeit.Timer("calc_total_improved(0, 1000)", setup="from __main__ import calc_total_improved").timeit(1)