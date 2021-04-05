# https://www.acmicpc.net/problem/2460

ls = [list(map(int, input().split())) for _ in range(10)]
num, max = 0, 0

for i in ls:
    num -= i[0]
    num += i[1]
    if num > max:
        max = num

print(max)