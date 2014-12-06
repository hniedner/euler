# Find the sum of all the multiples of 3 or 5 below 1000.
__author__ = 'hniedner@gmail.com'

total = 0
for x in range(0, 1000):
    if (x % 3 == 0) or (x % 5 == 0):
        total += x

print(total)

# Congratulations, the answer you gave to problem 1 is correct.
# You are the 414618th person to have solved this problem.