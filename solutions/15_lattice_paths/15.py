"""
Starting in the top left corner of a 2 * 2 grid, and only being able to move to the 
right and down, there are exactly 6 routes to the bottom right corner.

* see image *
How many such routes are there through a 20 * 20 grid?

"""

# NOTE: This would be the typical way to do this in python, since
# this formula is optimized in C. But for a math puzzle this is cheating
# as you'd learn nothing. For reference you can see it produces the same
# answer as the for loop down below.

import math

ans = math.comb(20 + 20, 20)
print(ans)


# <><><><><><><><><><><><><><><><><><><><><><><><>

# The "flag counting" trick
# Here we're using a classic math trick, known as "double counting" or
# "combinatorial proof". The core idea is that if you can find 2 ways to count
# the same thing, you can set them to be equal, and from there you can re-arrange
# the equation to find hacks.

# Say you're building a 20*i grid path (m fixed at 20, growing i by 1 each loop).
# Count all valid paths, but this time, for every path, also mark one specific "down" 
# move as "special" -- put a little flag on it. Since each path has exactly i down-moves, 
# you get i different marked versions of every path.

# We want to count "marked paths" (a normal path, plus a flag on one of its down-moves).
# There are two different ways to count this same set of things:

# Method A: Take every ordinary path, and for each one, put the flag on any of its
# i down-moves. Each path generates i marked versions.
# So total marked paths = result * i.

# Method B: Build the marked path from scratch a different way -- first pick which of the 
# m+i slots gets the flagged down-move (m+i choices), then fill in the rest of the path 
# using the previous smaller grid's path count.
# So total marked paths = (m+i) * previous_result.

# Both of these are counting the exact same collection of marked paths, just via 
# different logic -- one groups by "which path did this come from," the other groups 
# by "where's the flag." Since they're two routes to the same number, we know they
# must be equal to each other.
# This allows us to make this magic equation. It's simply (Method A) = (Method B):

# result * i = (m+i) * previous_result

# Now that we have this, we can re-arrange it:

# result = previous_result * (m+i) // i

# And now we have the equation we need to plug into the for loop below.


# <><><><><><><><><><><><><><><><><><><><><><><><>

# in the binomial coefficient, the width and height are traditionally
# designated as 'm' and 'n'.
m: int = 20
n: int = 20
result: int = 1

# this loop is walking through smaller versions of the grid, growing the "n" dimension 
# by 1 each iteration while keeping m fixed at 20. result after iteration i tells you 
# how many routes on a 20*i grid.
for i in range(1, n + 1):
    print(f"result = {result} * ({m} + {i}) // {i}")
    # You can see the result after every loop is a binomial coefficient

    result = result * (m + i) // i


print(f"\nResult is {result}")

# should be 137846528820

