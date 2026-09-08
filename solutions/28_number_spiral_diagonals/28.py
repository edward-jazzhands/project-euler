"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 
by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed 
in the same way?
"""

#  73 74 75 76 77 78 79 80 81 82
#  72 43 44 45 46 47 48 49 50
#  71 42 21 22 23 24 25 26 51
#  70 41 20  7  8  9 10 27 52
#  69 40 19  6  1  2 11 28 53
#  68 39 18  5  4  3 12 29 54
#  67 38 17 16 15 14 13 30 55
#  66 37 36 35 34 33 32 31 56
#  65 64 63 62 61 60 59 58 57


# 1 3 5 7 9 13 17 21 25 31 37 43 49 57 65 73 81 91 101 111 121
#   2 2 2 2  4  4  4  4  6  6  6  6  8  8  8  8 10  10  10  10
#       3x3         5x5         7x7         9x9          11x11
#                                           ...until 1001x1001


t = 1        # current target
i = 0        # iteration
y = 2        # step increase
p = 0        # pattern
t_sum = 1
size = 3
while size < 1002:

    i += 1
    t += y
    p += 1
    t_sum += t

    if p % 4 == 0:
        y += 2
        size += 2

print(t_sum)
