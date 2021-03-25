# https://codeup.kr/problem.php?id=6097

h, w = map(int, input().split())

board = [[0 for i in range(w)] for j in range(h)]

n = int(input())
for i in range(n):
    l, d, y, x = map(int, input().split())
    x -= 1
    y -= 1
    if d == 0:
        for l_len in range(l):
            board[y][x + l_len] = 1
    elif d == 1:
        for l_len in range(l):
            board[y + l_len][x] = 1

for y in range(h):
    for x in range(w):
        print(board[y][x], end=' ')
    print()