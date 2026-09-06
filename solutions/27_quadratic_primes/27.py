"""
Euler discovered the remarkable quadratic formula:
n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive 
integer values 0 <= n <= 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 
1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is 
clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 
primes for the consecutive values 0 <= n <= 79. The product of the 
coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:
n^2 + an + b, where |a| < 1000 and |b| <= 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, 
starting with n = 0.
"""

import math

def prime_checker(n: int) -> bool:
    # this check would be unnecessary if we're only inputting
    # odd numbers into the function
    if n % 2 == 0:
        return False

    sqrt = math.isqrt(n)

    for x in range(3, sqrt+1, 2):
        if n % x == 0:
            return False
    return True

assert prime_checker(25) is False
assert prime_checker(33) is False
assert prime_checker(17) is True
assert prime_checker(31) is True


most_primes = []
coefficients = (0, 0)

for i in range(-1000, 1001):
    for j in range(-1000, 1001):

        primes = []
        n = 0
        # loop until we hit one that is not prime
        while True:
            # print(f"z = {n}**2 + ({i}*{n}) + {j}")
            z = n**2 + (i*n) + j
            if z <= 0:  # can't be prime if less than 0
                break
            is_prime = prime_checker(z)
            if is_prime:
                primes.append(z)
            else:
                break
            n += 1
        
        if len(primes) > len(most_primes):
            most_primes = primes
            coefficients = (i, j)
            print(f"New winning coefficients:  {coefficients} | {len(most_primes) = }")
            
print()
print(f"Equation:  n**2 + ({coefficients[0]}*n) + {coefficients[1]}")
print(f"{coefficients = }")
print(f"Answer: {coefficients[0] * coefficients[1]}")