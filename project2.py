# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
__author__ = 'hannes'

import timeit


def fib(n):  # write Fibonacci series up to n
    print("Print a Fibonacci series up to " + str(n) + ".")
    t, a, b = 0, 0, 1
    while b < n:
        if b % 2 == 0:
            t += b
        a, b = b, a + b
    return t


print timeit.Timer("fib(4000000)", setup="from __main__ import fib").timeit(1)

#Congratulations, the answer you gave to problem 2 is correct.
#You are the 341466th person to have solved this problem.