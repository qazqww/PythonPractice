# https://www.acmicpc.net/problem/1292

start, end = map(int, input().split())
ls = [0]
num = 0

for i in range(1, 1000):
    for k in range(i):
        num += i
        ls.append(num)
        if len(ls) > end:
            print(ls[end] - ls[start-1])
            exit()