"""
The Fibonacci sequence is defined by the recurrence relation:
F(n) = F(n - 1) + F(n - 2), where F(1) = 1 and F(2) = 1.

Hence the first 12 terms will be:

F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
F(8) = 21
F(9) = 34
F(10) = 55
F(11) = 89
F(12) = 144

The 12th term, F(12), is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 
digits?
"""

from typing import Iterable

def fibonacci() -> Iterable[int]:

    x = 1
    y = 1
    while True:
        z = x + y
        x = y
        y = z
        # the first iteration yielded is F(3), which is 2
        yield z


for i, item in enumerate(fibonacci()):
    if len(str(item)) == 1000:
        print(f"answer: {i+3}")  # +3 because zero indexing and skip to F(3)
        break

