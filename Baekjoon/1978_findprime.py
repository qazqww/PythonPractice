# https://www.acmicpc.net/problem/1978

import math

N = int(input())
ls = list(map(int, input().split()))
largest = max(ls)

if 1 in ls:
    ls.remove(1)

remove_ls = []
for num in ls:
    if num != 2 and num % 2 == 0:
        remove_ls.append(num)
ls = list(set(ls).difference(remove_ls))


for i in range(3, math.ceil(math.sqrt(largest)) + 1, 2):
    remove_ls = []
    for num in ls:
        if num != i and num % i == 0:
            remove_ls.append(num)
    ls = list(set(ls).difference(remove_ls))

print(len(ls))