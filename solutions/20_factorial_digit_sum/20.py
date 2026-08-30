"""
n! means n * (n - 1) * ... * 3 * 2 * 1.
For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!.

"""

# NOTE: You can obviously just do 'from math import factorial' in python
# but doing so prevents you from learning anything. The factorial function
# is not difficult to write.

def factorial(n: int) -> int:

    prod = 1
    for x in range(n, 0, -1):        
        prod *= x
    return prod

j = factorial(100)
ans = sum([int(x) for x in list(str(j))])
print(ans)