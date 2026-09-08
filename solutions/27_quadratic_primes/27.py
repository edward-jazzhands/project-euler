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
import time
# import sys

def prime_checker(n: int) -> bool:
    if n == 1:
        return False
    if n == 2:
        return True
        
    # this check would be unnecessary if we're only inputting
    # odd numbers into the function:
    if n % 2 == 0:
        return False

    sqrt = math.isqrt(n)

    for x in range(3, sqrt+1, 2):
        if n % x == 0:
            return False
    return True


# puzzle says |a| < 1000 and |b| <= 1000
# that means a is between -999 and 999
# while b is between -1000 and 1000

# HOWEVER, we don't actually need to start b at -1000.
# Because it always starts each look with n=0, when that is plugged into
# the equation, you'll get: n**0 + a*0 + b, which of course is just 'b'.

# So if b is not prime, it would break after 1 loop.
# And since we know the first prime number is 2, this means logically
# that b cannot be less than 2. It also must be odd (all primes are odd).

# We ALSO know that a must be odd as well! This is because at n=1,
# you will get: n**1 (which is 1) + a*1 (which is a) + b
# this simplifies to `1 + a + b`.
# We already know b must be odd, and 1 + any odd will make an even number.
# Logically this means 1 must also be odd, to flip the result back to being odd.
# if not, it will fail on the second loop. So we can skip those as well.

start = time.time()

most_primes = 0
coefficients = (0, 0)

# pre-generate the primes list for the b coefficient
prime_Bs = [2] + [b for b in range(3, 1001, 2) if prime_checker(b)]

for a in range(-999, 1000, 2):
    for b in prime_Bs:

        primes = 0

        n = 0
        # loop until we hit one that is not prime
        while True:
            # print(f"z = {n}**2 + ({i}*{n}) + {j}")   # enable for debug

            # while loop here is pretty simple - plug a and b into the equation,
            # check if the result is a prime number. Keep going until it
            # hits one that is not prime. Then check if we have a new winner.

            z = n**2 + (a*n) + b

            if z <= 0:  # can't be prime if less than 0
                break
            is_prime = prime_checker(z)
            if is_prime:
                primes += 1
            else:
                break
            n += 1
        
        if primes > most_primes:
            most_primes = primes
            coefficients = (a, b)
            # print(f"New winning coefficients:  {coefficients} | {len(most_primes) = }")
            
print()
print(f"Equation:  n**2 + ({coefficients[0]}*n) + {coefficients[1]}")
print(f"{coefficients = }")
print(f"Answer: {coefficients[0] * coefficients[1]}")

end = time.time() - start
print(f"Time taken: {end:.5f}")