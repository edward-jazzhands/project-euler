"""
A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors of 28 
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. By 
mathematical analysis, it can be shown that all integers greater than 28123 can 
be written as the sum of two abundant numbers. However, this upper limit cannot 
be reduced any further by analysis even though it is known that the greatest 
number that cannot be expressed as the sum of two abundant numbers is less than 
this limit.
Find the sum of all the positive integers which cannot be written as the sum of 
two abundant numbers.
"""

# the greatest number that cannot be expressed as the sum of two abundant numbers
# is less than 28123

import math
import time

def get_factors(n: int) -> list:
    factors = [1]     # 1 is always a factor
    isqrt = math.isqrt(n)   # use isqrt instead of sqrt for looping
    for i in range(2, isqrt+1):
        if n % i == 0:
            if i == n // i:  # this means i is the square root of n
                factors.append(i)
            else:
                factors.append(i)
                factors.append(n // i)
                
    factors.sort()
    return factors

def is_abundant(n: int) -> bool:

    factors = get_factors(n)
    f_sum = sum(factors)
    if f_sum > n:
        return True
    else:
        return False

# Find the sum of all the positive integers which 
# cannot be expressed as the sum of two abundant numbers.

# we know the greatest number that cannot be expressed as the sum of two abundant numbers
# is less than 28123
# which means when finding the abundant numbers to check against, we only need to collect
# up to 28123.

start = time.time()

abundants = []
for n in range(1, 28123):
    if is_abundant(n):
        abundants.append(n)

# pre-load the entire cache - takes about 5 seconds
print("starting cache pre-load")
abundant_sums: set[int] = set()
for x in abundants:
    for y in abundants:
        z = x + y
        if z not in abundant_sums:
            abundant_sums.add(z)

print("finished cache pre-load")

total = 0
for n in range(1, 28123):
    if n not in abundant_sums:
        total += n

print(total)
print(f"Total script time:  {time.time() - start:.2f}")

