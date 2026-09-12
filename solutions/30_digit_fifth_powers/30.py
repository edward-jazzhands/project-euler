"""
Surprisingly there are only three numbers that can be written as the sum of 
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4\\
8208 = 8^4 + 2^4 + 0^4 + 8^4\\
9474 = 9^4 + 4^4 + 7^4 + 4^4


<p class="smaller">As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers 
of their digits.


"""

winners = []
for n in range(10000000, 20000000):
    # break the integer up
    if n % 100000 == 0:
        print("passing ", n)


    n_broken: list[int] = [int(x) for x in str(n)]
    
    summed = 0
    for x in n_broken:
        summed += x**5

    if summed == n:
        winners.append(n)

print(winners)
print(sum(winners))
