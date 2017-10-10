# https://www.hackerrank.com/challenges/a-very-big-sum

import sys

def aVeryBigSum(n, ar):
    sum = 0
    for item in ar:
        sum += item
    return sum


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)