"""
2^{15} = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^{1000}?

"""

x = 2 ** 1000
strx = str(x)
list_strx = list(strx)
list_intx = [int(x) for x in list_strx]
ans = sum(list_intx)
print(ans)

# code golfing:
print(sum([int(x) for x in list(str(2 ** 1000))]))

# should be 1366

