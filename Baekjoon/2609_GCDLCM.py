# https://www.acmicpc.net/problem/2609

n1, n2 = map(int, input().split())
big, small = max(n1, n2), min(n1, n2)
r = 1

while r != 0:
    r = big % small
    big = small
    small = r

print(big)
print(int(n1 * n2 / big))