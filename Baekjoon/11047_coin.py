# https://www.acmicpc.net/problem/11047

coin_list = []
count = 0
N, K = map(int, input().split())
for i in range(N):
    coin_list.append(int(input()))

coin_list.reverse()
for coin in coin_list:
    if K >= coin:
        count += K // coin
        K = K % coin
    if K == 0:
        break

print(count)