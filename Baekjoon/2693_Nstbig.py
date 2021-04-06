# https://www.acmicpc.net/problem/2693

T = int(input())
for _ in range(T):
    ls = list(map(int, input().split()))
    ls.sort()
    print(ls[7])