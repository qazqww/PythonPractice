# https://codeup.kr/problem.php?id=4060

from sys import stdin

def check_connection(x, y, num):
    if y+1 < col and bulb[y+1][x] == num:
        bulb[y+1][x] = -1
        check_connection(x, y+1, num)
    if y-1 >= 0 and bulb[y-1][x] == num:
        bulb[y-1][x] = -1
        check_connection(x, y-1, num)
    if x+1 < row and bulb[y][x+1] == num:
        bulb[y][x+1] = -1
        check_connection(x+1, y, num)
    if x-1 >= 0 and bulb[y][x-1] == num:
        bulb[y][x-1] = -1
        check_connection(x-1, y, num)

bulb = []
area_onoff = [0, 0]
col, row = map(int, stdin.readline().split())
for i in range(col):
    bulb.append(list(map(int, stdin.readline().split())))

for y in range(col):
    for x in range(row):
        if bulb[y][x] != -1:
            temp = bulb[y][x]
            check_connection(x, y, bulb[y][x])
            area_onoff[temp] += 1

print(area_onoff[0], area_onoff[1])