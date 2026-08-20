"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting 
numbers finish at 1.

Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import time

start = time.time()

# seeding the cache with 1:1 is necessary
# otherwise we'd need to check if n == 1 every loop
cache: dict[int, int] = {1: 1}

# NOTE: The recursive version actually benches slightly faster
def chain_length_recursive(n: int) -> int:
    if n in cache:
        return cache[n]
    if n % 2 == 0:
        result = 1 + chain_length_recursive(n // 2)
    else:
        result = 1 + chain_length_recursive(3 * n + 1)
    cache[n] = result
    return result


def chain_length(n: int) -> int:
    steps = []
    while n not in cache:
        steps.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    result = cache[n]
    # now for each entry in the steps, work backwards and add 1 each time
    for s in reversed(steps):
        result += 1
        cache[s] = result
    return result



longest_chain = 0
winner = 0
for i in range(1, 1_000_000):
    chain = chain_length_recursive(i)
    # chain = chain_length(i)
    if chain > longest_chain:
        longest_chain = chain
        winner = i
        print(f"new winner: {winner} - chain length: {longest_chain}")

print()
print(f"Final Winner: {winner} - chain length: {longest_chain}")
# ans is 837799


end = time.time() - start
print(f"took {end:.2f} seconds")
