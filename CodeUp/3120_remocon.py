# https://codeup.kr/problem.php?id=3120

cur, target = map(int, input().split())
gap = abs(target - cur)
cnt = 0

while gap >= 10:
    gap -= 10
    cnt += 1

# n - 5 - k가 빠르냐
# n - 10 + k가 빠르냐

if abs(gap - 10) < 3:
    gap = abs(gap - 10)
    cnt += 1

while gap >= 5:
    gap -= 5
    cnt += 1

# n - k가 빠르냐
# n - 5 + k가 빠르냐

if abs(gap - 5) < 2:
    gap = abs(gap - 5)
    cnt += 1

cnt += gap

print(cnt)