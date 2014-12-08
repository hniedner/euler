# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
__author__ = 'hannes'
import math
import time

startTime = time.clock()
print "Calculating..."


def calc_prime(n):  # calculates range (largest) not nth prime
    a = [1] * n
    for i in xrange(2, int(math.sqrt(n) + 1)):
        if a[i]:
            for j in xrange(i * i, n, i):
                a[j] = 0
    return [i for i in xrange(len(a)) if a[i] == 1][2:]


print "sum is ->> " + str(reduce(lambda x, y: x + y, calc_prime(2000000)))
print "My Program took %.4f secs to execute\n" % (time.clock() - startTime)


# You are the 164744th person to have solved this problem.
# You have earned 1 new award:
# Decathlete: Solve ten consecutive problems