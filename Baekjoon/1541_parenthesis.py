# https://www.acmicpc.net/problem/1541

expr = input().split('-')

for i in range(len(expr)):
    temp = map(int, expr[i].split('+'))
    expr[i] = sum(temp)
    
result = expr[0]
for i in range(1, len(expr)):
    result -= expr[i]

print(result)