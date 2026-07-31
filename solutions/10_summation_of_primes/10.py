"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""

# import math
# import time

# start = time.time()
# def prime_checker(n: int) -> bool:
#     # NOTE: only passing in odd numbers makes this
#     # function do 1/2 the work.
    
#     # Without this, if you passed in even numbers, this would
#     # return the wrong answer:
#     if n % 2 == 0:
#         return False
    
#     sqroot = int(math.sqrt(n))
#     # increment by 2 - we only need to check if n
#     # is divisible by odd numbers.

#     for x in range(3, sqroot+1, 2): # inclusive stop
#         if n % x == 0:
#             return False  # number is not prime
#     # if we make it through loop then n is prime
#     return True
    
# primes_sum = 2 # 2 is only even prime, so pre-include

# i = 3   # don't include 1 or 2
# while i < 2000000:
#     if prime_checker(i):
#         primes_sum += i
#     i += 2  # increment by 2 - only check odd numbers
#     # NOTE: incrementing by odd numbers here should hypothetically
#     # reduce the amount of work but in practice it seems to have
#     # absolutely no effect.
    
# print(primes_sum)
# # we already know the right answer so this just ensures it worked:
# print((primes_sum == 142913828922))
# print(f"Elapsed: {time.time() - start}")



# METHOD 2 - SIEVE OF ERATOSTHENES

import time

start = time.time()

def sieve_of_eratosthenes(limit: int):
    # Create a boolean array and initialize all as True
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            # Mark all multiples of i as not prime
            for j in range(i*i, limit, i):
                is_prime[j] = False
    
    # Sum all numbers where is_prime is True
    return sum(i for i in range(limit) if is_prime[i])

primes_sum = sieve_of_eratosthenes(2000000)
print(primes_sum)
print((primes_sum == 142913828922))
print(f"Elapsed: {time.time() - start}")