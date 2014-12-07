# Special Pythagorean triplet
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# natural numbers == whole numbers
__author__ = 'hannes'
import math
import timeit
# a < b < c
# a + b + c == 1000
# a*a + b*b == c*c


def find_millennium_triplet():  # calculating the sqrt takes longer
    m = 1000
    a, b = 1, 2
    for a in xrange(1, m / 3):
        for b in xrange(a + 1, m / 2):
            c = math.sqrt(a * a + b * b)
            if c > b and a + b + c == 1000:
                print int(a * b * c)
    return 0


def sof():  # http://stackoverflow.com/questions/2817848/find-pythagorean-triplet-for-which-a-b-c-1000
    m = 1000
    for a in xrange(1, m / 3):
        for b in xrange(a + 1, m / 2):
            c = m - a - b
            if a * a + b * b == c * c:
                print a * b * c
    return 0


print timeit.Timer("find_millennium_triplet()", setup="from __main__ import find_millennium_triplet").timeit(1)
print timeit.Timer("sof()", setup="from __main__ import sof").timeit(1)

# Congratulations, the answer you gave to problem 9 is correct.
# You are the 179616th person to have solved this problem.