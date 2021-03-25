# https://codeup.kr/problem.php?id=2001

pasta = []
juice = []
min = 10000

for i in range(3):
    pasta.append(int(input()))
for i in range(2):
    juice.append(int(input()))

for p in pasta:
    for j in juice:
        if (p + j) < min:
            min = p + j

print(round(min * 1.1, 3))