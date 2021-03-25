# https://www.acmicpc.net/problem/1931
# 반례를 찾는 데에 고생했던 문제
# 입력이 많을 때엔 input()보다 stdin.readline()이 훨씬 빠르다

from sys import stdin

N = int(input())
time = []
now, count = 0, 0

for i in range(N):
    temp1, temp2 = map(int, stdin.readline().split())
    time.append((temp1, temp2))

time.sort(key=lambda x:(x[1], x[0]))
for i in range(len(time)):
    if now <= time[i][0]:
        now = time[i][1]
        count += 1
        
print(count)