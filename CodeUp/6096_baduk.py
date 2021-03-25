# https://codeup.kr/problem.php?id=6096

baduk_list = []

for i in range(19):
    baduk_list.append(list(map(int, input().split())))

cnt = int(input())

for i in range(cnt):
    x, y = map(int, input().split())
    for num in range(19):
        baduk_list[num][y - 1] = 1 - baduk_list[num][y - 1]
        baduk_list[x - 1][num] = 1 - baduk_list[x - 1][num]

for i in range(19):
    for j in range(19):
        print(baduk_list[i][j], end=' ')
    print()