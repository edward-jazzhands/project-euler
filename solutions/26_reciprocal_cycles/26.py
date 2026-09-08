"""
A unit fraction contains 1 in the numerator. The decimal representation of the 
unit fractions with denominators 2 to 10 are given:

1/2 = 0.5
1/3 =0.(3)
1/4 =0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be 
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle 
in its decimal fraction part.
"""

from decimal import Decimal, getcontext
import time


# VERSION 1: My original version

# NOTE: 2000 is the minimum precision to get the correct answer in this puzzle
getcontext().prec = 2000


def find_repeat(s: str) -> str | None:

    n = len(s)
    x = n // 2

    for j in range(x + 1):
        for i in range(1, x + 1):
            window1 = s[j:i+j]
            all_match = True
            for k in range(1, n // len(window1)):
                window2 = s[(i*k)+j:(i*(k+1))+j]

                # line by line imagine it like this:
                # window2 = s[(i*1)+j:((i*2))+j]
                # window3 = s[(i*2)+j:((i*3))+j]
                # window4 = s[(i*3)+j:((i*4))+j]

                # print(f"{window1 = } | {window2 = }")
                if window2 != window1 and window2 != "":
                    all_match = False
                    break
            if all_match:
                return window1

    return None

start1 = time.time()

longest = ""
iteration = 0

for i in range(2, 1000):
    x = Decimal(1) / Decimal(i)

    decimals = str(x).split(".")[1]
    decimals = decimals[:-1] # remove the last digit because of the rounding 
    repeats = find_repeat(decimals)
    if repeats:
        if len(repeats) > len(longest):
            longest = repeats
            # print(f"\033[34m new longest pattern for {i}: \033[0m {len(repeats)}")
            iteration = i

end1 = time.time() - start1
print(f"Time taken: {end1:.5f}")

print(f"\nAnswer: {iteration = }, had length: {len(longest)}")
    

# -----------------------------------------------------

# VERSION 2: Better solution (copied):

# This version uses a cool math trick, which is very simple once you understand
# how it works. It is significantly faster, roughly from O(n^2) down to O(n)

def recurring_cycle_length(d: int) -> int:
    remainder = 1
    seen = {}

    position = 0

    while remainder:  # stops if remainder = 0
        if remainder in seen:
            # the length of the pattern will be the current position minus the
            # last time this remainder was seen
            return position - seen[remainder]

        seen[remainder] = position

        remainder *= 10
        remainder %= d
        position += 1

    # loop only stops if remainder is 0, so just return 0
    return 0

    # NOTE: This is literally doing long division but expressed as python
    # Using d=7 for example:
    # position 0:  remainder=(1*10)=10 | remainder % d == 3  (10-7=3)  - decimal 1
    # position 1:  remainder=(3*10)=30 | remainder % d == 2  (30-28=2) - decimal 4
    # position 2:  remainder=(2*10)=20 | remainder % d == 6  (20-14=6) - decimal 2
    # position 3:  remainder=(6*10)=60 | remainder % d == 4  (60-56=4) - decimal 8
    # position 4:  remainder=(4*10)=40 | remainder % d == 5  (40-35=5) - decimal 5
    # position 5:  remainder=(5*10)=50 | remainder % d == 1  (50-49=1) - decimal 7
    # position 6:  remainder=(1*10)=10 | remainder % d == 3  (10-7=3)  - decimal 1

    # In long-hand to make it extra clear:

    #       0.1428571
    #      -----------------
    #   7 / 1 0000000
    #         7
    #       ----
    #         30
    #         28
    #       ----
    #          20
    #          14
    #         ----
    #           60
    #           56
    #          ----
    #            40
    #            35
    #           ----
    #             50
    #             49
    #            ----
    #              10
    #               7

    # This works because using long division, once we see the same number again,
    # we know mathematatically it must repeat the same pattern from that point.
    # This means we only need to track remainders we have seen, and the pattern is found
    # as soon as we see any remainder twice.
    # This greatly reduces the amount of calculations needed compared to
    # the first version, it brings it from O(n^2) down to O(n).

start2 = time.time()##

longest = 0
answer = 0

for d in range(2, 1000):
    length = recurring_cycle_length(d)

    if length > longest:
        longest = length
        answer = d


end2 = time.time() - start2
print(f"Time taken: {end2:.5f}")
