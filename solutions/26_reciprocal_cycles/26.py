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

print(f"\nAnswer: {iteration = }, had length: {len(longest)}")
    
