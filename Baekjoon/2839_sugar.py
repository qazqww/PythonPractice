# https://www.acmicpc.net/problem/2839

target = int(input())

five_max = target // 5
five, three = -1, -1
k = 0

while five_max - k >= 0:
    temp = target - (five_max - k) * 5
    if temp % 3 == 0:
        print(five_max - k + temp // 3)
        exit()
    k += 1

print(-1)