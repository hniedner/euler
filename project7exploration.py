__author__ = 'hannes'
import math
import timeit

# http://codegolf.stackexchange.com/questions/6309/list-of-first-n-prime-numbers-most-efficiently-and-in-shortest-code


def calc_prime(n):  # calculates range (largest) not nth prime
    a = [1] * n
    for i in xrange(2, int(math.sqrt(n) + 1)):
        if a[i]:
            for j in xrange(i * i, n, i):
                a[j] = 0
    print [i for i in xrange(len(a)) if a[i] == 1][2:]


print timeit.Timer("calc_prime(104744)", setup="from __main__ import calc_prime").timeit(1)


def prime_generator(n):  # n - number of primes to generate
    l = [1] * n
    l[0], l[1] = 2, 3
    for x in xrange(2, n):
        l[x] += l[x - 1] + 1
        while all(l[x] % i for i in xrange(2, int(math.sqrt(l[x]) + 1))) is False:
            l[x] += 2
    print l


print timeit.Timer("prime_generator(10001)", setup="from __main__ import prime_generator").timeit(1)