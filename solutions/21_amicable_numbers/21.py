"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and 
each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 
142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""

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
                pair = n // i
                factors.append(i)
                factors.append(pair)
                # NOTE: We know it is 2 factors each time, except for the square root of n.
                # if i is a factor of n (eg. n % i == 0), then it means n // i must also
                # be a factor. For example, 100 % 2 == 0 (2 is a factor), so 100 / 2 (50)
                # is also a factor. Thus we increment by 2 instead of 1, each time.
                # this trick makes this function significantly faster because we only
                # have to check up to the square root of n instead of half-way.
                
    factors.sort()
    return factors


found_pairs = {}

for i in range(1, 10001):

    if found_pairs.get(i):
        continue

    factors = get_factors(i)
    x = sum(factors)
    pair_factors = get_factors(x)
    y = sum(pair_factors)

    if y == i and x != i:
        found_pairs[i] = x
        found_pairs[x] = i


print()
for k, v in found_pairs.items():
    print(f"{k}: {v}")

print()
print(f"answer:  {sum(found_pairs)}")