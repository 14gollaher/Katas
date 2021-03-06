# https://www.hackerrank.com/challenges/diagonal-difference
import sys

def solve(n, a):
    diagonalOneSum = 0
    diagonalTwoSum = 0
    for i in range(n):
        diagonalOneSum += a[i][i]
        diagonalTwoSum += a[i][n - i - 1]
    return str(abs(diagonalOneSum - diagonalTwoSum))

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
print(solve(n, a))
