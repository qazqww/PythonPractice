# https://www.acmicpc.net/problem/5585

change = 1000 - int(input())
money_list = [500, 100, 50, 10, 5, 1]
count = 0

for money in money_list:
    if change >= money:
        count += change // money
        change = change % money
    if change == 0:
        break

print(count)