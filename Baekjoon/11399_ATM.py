# https://www.acmicpc.net/problem/11399

num = int(input())
time = list(map(int, input().split()))

time.sort()
for i in range(1, len(time)):
    time[i] += time[i - 1]

print(sum(time))