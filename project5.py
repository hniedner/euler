# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
__author__ = 'hannes'


def gcd(x, y):  # calculate greatest common divisor of x and y
    while y != 0:
        (x, y) = (y, x % y)
    return x


def lcm(x, y):  # calculate least common multiple of x and y
    return x / gcd(x, y) * y


print reduce(lcm, range(1, 20))


# thanks to web
# Congratulations, the answer you gave to problem 5 is correct.
# You are the 238713th person to have solved this problem.