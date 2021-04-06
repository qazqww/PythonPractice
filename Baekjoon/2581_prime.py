# https://www.acmicpc.net/problem/2581

import math

M, N = int(input()), int(input())
ls = []

if M <= 2 and N >= 2:
    ls.append(2)

if M % 2 == 0:
    M += 1

for i in range(M, N+1, 2):
    passed = True
    for num in range(3, int(math.ceil(math.sqrt(i) + 1)), 2):
        if i % num == 0:
            passed = False
            break
    if passed:
        ls.append(i)

if 1 in ls:
    ls.remove(1)

if len(ls) == 0:
    print("-1")

else:
    print("{}\n{}".format(sum(ls), ls[0]))