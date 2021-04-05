# https://www.acmicpc.net/problem/2501

N, K = map(int, input().split())
cnt = 0

for i in range(1, int(N/2) + 1):
    if N % i == 0:
        cnt += 1
        if (cnt == K):
            print(i)
            exit()

if cnt == K - 1:
    print(N)

else:
    print(0)