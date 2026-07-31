"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# import math
# import time

# start = time.time()

# c_sqrt = 5
# answer = 0
# while True:
#     c_squared = c_sqrt**2
#     print(f"Checking {c_sqrt}...")
    
#     a_squared = 1
#     full_break = False
#     while a_squared <= c_squared // 2:  # past halfway it would just be same numbers reversed
#         b_squared = c_squared - a_squared    # Example: 24=25-1 | 23=25-2 | etc 
#         a_sqrt = math.sqrt(a_squared)
#         b_sqrt = math.sqrt(b_squared)
#         if a_sqrt.is_integer() and b_sqrt.is_integer() \
#         and (a_sqrt + b_sqrt + c_sqrt == 1000):
#             print(f"{int(a_sqrt)} + {int(b_sqrt)} + {c_sqrt} = 1000")
#             answer = a_sqrt*b_sqrt*c_sqrt
#             full_break = True
#             break
#         a_squared += 1      # increase a_squared for next loop
#     if full_break:
#         break
#     c_sqrt += 1          # no full break, increase c and continue
    
# print(int(answer))
# print(f"Time elapsed: {time.time() - start}")


# import time

# start = time.time()

# # We know: a + b + c = 1000 and a² + b² = c²
# # So: b = 1000 - a - c
# # Substituting into a² + b² = c²:
# # a² + (1000 - a - c)² = c²

# for a in range(1, 500):  # a must be less than 500 (since a < b < c and a+b+c=1000)
#     for c in range(a + 2, 1000 - a):  # c must be > a+1 and < 1000-a
#         b = 1000 - a - c
#         if b > a and b < c and a*a + b*b == c*c:
#             print(f"{a} + {b} + {c} = 1000")
#             print(f"Product: {a * b * c}")
#             print(f"Time elapsed: {time.time() - start}")
#             exit()
            
            
import time

start = time.time()

# From a + b + c = 1000, we get: b = 1000 - a - c
# From a² + b² = c², we get: a² + (1000 - a - c)² = c²
# Expanding: a² + 1000000 - 2000a - 2000c + a² + 2ac + c² = c²
# Simplifying: 2a² + 2ac - 2000a - 2000c + 1000000 = 0
# Rearranging: c = (1000000 - 2000a + 2a²) / (2000 - 2a)
# Simplifying: c = (500000 - 1000a + a²) / (1000 - a)

for a in range(1, 500):
    c_numerator = 500000 - 1000*a + a*a
    c_denominator = 1000 - a
    
    if c_numerator % c_denominator == 0:  # c must be an integer
        c = c_numerator // c_denominator
        b = 1000 - a - c
        
        if a < b < c and a*a + b*b == c*c:
            print(f"{a}² + {b}² = {c}²")
            print(f"{a} + {b} + {c} = 1000")
            print(f"Product: {a * b * c}")
            print(f"Time elapsed: {time.time() - start}")
            break