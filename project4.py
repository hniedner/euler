# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
__author__ = 'hniedner@gmail.com'


def is_palindrome(n):  # n number or string to be tested
    f = str(n)
    l = list(f)
    l.reverse()
    r = "".join(l)
    return f == r


def find_largest_palindrome(l):  # number of digits in factors > 0
    lower = 10 ** (l - 1) - 1  # lower boundary l = 1 -> 0, l = 2 -> 9, l = 3 -> 99 etc.
    upper = 10 ** l - 1  # upper boundary l = 1 -> 9, l = 2 -> 99, l = 3 -> 999 etc.
    f1, f2, m = 0, 0, 0  # factor 1, factor 2, max value

    for x in range(upper, lower, -1):
        stop = False
        for y in range(upper, lower, -1):
            p = x * y
            if is_palindrome(p):
                if p > m:
                    m = p
                    f1, f2 = x, y

    print("f1 = " + str(f1))
    print("f2 = " + str(f2))
    return m


print("Largest palindrome: " + str(find_largest_palindrome(3)))

# Congratulations, the answer you gave to problem 4 is correct.
# You are the 225569th person to have solved this problem.