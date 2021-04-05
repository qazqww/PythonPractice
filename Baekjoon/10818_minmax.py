# https://www.acmicpc.net/problem/10818

from sys import stdin

N = int(input())
ls = list(map(int, stdin.readline().split()))
min, max = 1000001, -1000001

for num in ls:
    if num < min:
        min = num
    if num > max:
        max = num

print(min, max)