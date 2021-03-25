# https://codeup.kr/problem.php?id=3321

topps = []
topp_cnt = int(input())
dough_price, topp_price = map(int, input().split())
dough_kcal = int(input())
for i in range(topp_cnt):
    topps.append(int(input()))

sum_kcal = dough_kcal
sum_price = dough_price
topps.sort(reverse=True)

for topp_kcal in topps:
    if sum_kcal / sum_price < topp_kcal / topp_price:
        sum_kcal += topp_kcal
        sum_price += topp_price

print(int(sum_kcal / sum_price))