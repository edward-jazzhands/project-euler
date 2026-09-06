"""
A permutation is an ordered arrangement of objects. For example, 3124 is one 
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations 
are listed numerically or alphabetically, we call it lexicographic order. The 
lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 
6, 7, 8 and 9?
"""

import time

# VERSION ONE: ITERTOOLS
# This is implemented in C under the hood, it's how you'd typically do this
# in Python. Some langauges do not have this built in.

import itertools

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



start = time.time()

combos = itertools.permutations(digits)

target = 0
for item in combos:
    target += 1
    if target == 1000000:
        ans = ""
        for x in item:
            ans += str(x)
        print(ans)
        break

print(f"VERSION ONE time:  {time.time() - start:.8f}")

# VERSION TWO: PURE PYTHON
# This is showing the same algorithm that itertools uses, but implemented
# in pure python for demonstration. Its much slower than itertools.
# Here it takes about 2 seconds (vs 0.02 for itertools)

from typing import TypeVar, Iterable, Iterator

T = TypeVar("T")


def permutations(
    iterable: Iterable[T],
    r: int | None = None,
) -> Iterator[tuple[T, ...]]:
    

    pool = tuple(iterable)
    n = len(pool)

    if r is None:
        r = n

    if r > n or r < 0:
        return

    indices = list(range(n))
    cycles = list(range(n, n - r, -1))

    yield tuple(pool[i] for i in indices[:r])

    while n:
        for i in range(r - 1, -1, -1):
            cycles[i] -= 1

            if cycles[i] == 0:
                # Rotate indices[i:] left by one
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

start = time.time()
combos2 = permutations(digits)

# should give same answer as itertools
target = 0
for item in combos2:
    target += 1
    if target == 1000000:
        ans = ""
        for x in item:
            ans += str(x)
        print(ans)
        break

print(f"VERSION TWO time:  {time.time() - start:.8f}")

# VERSION THREE: The pro method
# The actual pro way to solve this problem involves a cool math trick.
# This is faster than even using itertools.permutations even though this is
# in python and itertools is using C.
# itertools.permutations benched at 0.1 seconds to reach the 1 millionth
# permutation. This function solves the question in 0.002 seconds. In a
# compiled language you can imagine it would be virtually instantaneous.

# NOTE: Explanation at the bottom

import math

def get_nth_permutation(digits: list[int], n: int) -> str:
    
    # Convert to 0-indexed position (e.g. 1,000,000th item is index 999,999)
    k: int = n - 1

    # making a copy here just so we don't modify mutable inputs
    available: list[int] = digits.copy()
    result: list[str] = []

    for i in range(len(digits) - 1, -1, -1):
        factorial: int = math.factorial(i)
        
        # Determine which element from 'available' goes next
        index: int = k // factorial
        result.append(str(available.pop(index)))
        
        # Update k to the remainder position within the chosen block
        k %= factorial

    return "".join(result)

start = time.time()
print(get_nth_permutation(digits, 1000000))

print(f"VERSION THREE time:  {time.time() - start:.8f}")


# EXPLANATION (courtesy of Gemini):
"""
Think of listing all permutations in order like organizing a phone book or a dictionary.

Since we have 10 digits (`0` through `9`), every permutation is a 10-digit number.
When we list them alphabetically (lexicographically), they naturally group into 
alphabetical "blocks" based on their first digit:

* Block 0: All numbers starting with `0` (e.g., `0123456789` to `0987654321`)
* Block 1: All numbers starting with `1` (e.g., `1023456789` to `1987654321`)
* Block 2: All numbers starting with `2` (e.g., `2013456789` to `2987654321`)
* ...and so on, up to Block 9.

To figure out how many numbers are in Block 0, we fix `0` as the first digit. 
That leaves 9 digits (`1` through `9`) to arrange in all possible orders.

The total number of ways to arrange 9 items is 9! (9 factorial), which is:

9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 362,880

Every block has exact same size (362,880 numbers).

Now, if you line up the full list of numbers from 1 to 3,628,800 and walk down 
the list counting up to item #1,000,000:

1. Block 0 covers items #1 to #362,880. All of these start with `0`. 
   (Item #1,000,000 hasn't appeared yet, so keep going).
2. Block 1 covers the next 362,880 items, which is #362,881 to #725,760. 
   All of these start with `1`. (Still haven't reached #1,000,000).
3. Block 2 covers the next 362,880 items, which is #725,761 to #1,088,640. 
   All of these start with `2`.

Because #1,000,000 falls right between 725,761 and 1,088,640, the 1,000,000th 
item must lie inside Block 2. And every single number inside Block 2 starts with `2`.

By subtracting the blocks of 9! you passed, you reduce the target index and repeat 
the exact same process for the remaining available digits using 8!, then 7!, down to 0!.
"""