# https://codeup.kr/problem.php?id=2698
# 시간 개선 필요

def rev(ls):
    temp = []
    for i in range(len(ls)):
        k = len(ls) - i - 1
        temp.append((ls[k][0], ls[k][2], ls[k][1]))
    return temp

n = int(input())
ls = [(1, 'A', 'B'), (1, 'B', 'C')]
for i in range(n - 1):
    ls = ls + [(i + 2, 'A', 'B')] + rev(ls) + [(i + 2, 'B', 'C')] + ls

for move in ls:
    print("{} : {}->{}".format(move[0], move[1], move[2]))
print(len(ls))