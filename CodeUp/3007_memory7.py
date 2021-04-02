# https://codeup.kr/problem.php?id=3007

from sys import stdin

n, m = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
sums = [0]

for i in range(len(nums)):
    sums.append(sums[i] + nums[i])

for i in range(m):
    a, b = map(int, stdin.readline().split())
    print(sums[b] - sums[a-1])