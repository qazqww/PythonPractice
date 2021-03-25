# https://codeup.kr/problem.php?id=6098

house = []
cur_y = 1
cur_x = 1

for i in range(10):
    house.append(list(map(int, input().split())))

while True:
    if house[cur_y][cur_x] == 2:
        house[cur_y][cur_x] = 9
        break

    house[cur_y][cur_x] = 9
    if house[cur_y][cur_x + 1] != 1:
        cur_x += 1
    elif house[cur_y + 1][cur_x] != 1:
        cur_y += 1
    else:
        break

for y in range(10):
    for x in range(10):
        print(house[y][x], end=' ')
    print()