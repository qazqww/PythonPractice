# https://codeup.kr/problem.php?id=3703

candy_map = []
y, x = map(int, input().split())
for i in range(y):
    candy_map.append(list(map(int, input().split())))

for i in range(1, y + x - 1):
    for j in range(0, i + 1):
        if j >= y or i-j >= x:
            continue
        top = candy_map[j - 1][i - j] if j - 1 >= 0 else -1
        left = candy_map[j][i - j - 1] if i - j - 1 >= 0 else -1
        candy_map[j][i-j] += top if top > left else left

print(candy_map[y-1][x-1])