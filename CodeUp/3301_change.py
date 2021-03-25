# https://codeup.kr/problem.php?id=3301

change = int(input())
cnt = 0
money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for m in money_list:
    cnt += change // m
    change = change % m

print(cnt)