# https://codeup.kr/problem.php?id=4684
# 완벽한 풀이가 되질 않아서 더 연구해야 함

# num = int(input())
# serial = list(map(int, input().split()))
temp_start = -1

num = 10
# serial = [8, 6, 5, 4, 3, 2, 1, 10, 9, 7]
# serial = [9, 2, 1, 10, 3, 4, 5, 6, 7, 8]
serial = [1, 10, 9, 8, 3, 4, 5, 6, 7, 2]

# 정리된 구간이 먼저 오도록 정리, temp_start만큼 또 이동된 상태
for i in range(len(serial) - 1):
    if serial[i] + 1 != serial[i + 1]:
        continue
    temp_start = i
    break

if temp_start == -1:
    temp_start = len(serial) - 1

temp_serial = serial[temp_start:] + serial[:temp_start]

# 거꾸로 된 구간을 원래대로 하여 얼마나 이동되었는지 구하려는 과정
for i in range(len(temp_serial) - 1):
    if temp_serial[i] + 1 != temp_serial[i+1] or (temp_serial[i] == num and temp_serial[i+1] != 1):
        first = i + 1
        break

last = len(temp_serial) - 1
for i in range(len(temp_serial) - first - 1):
    if not (temp_serial[first + i] - 1 == temp_serial[first + i + 1]) and not (temp_serial[first + i] == 1 and temp_serial[first + i + 1] == num):
        last = first + i
        break

rev_list = temp_serial[first:last+1]
rev_list.reverse()
for i in range(first, last+1):
    temp_serial[i] = rev_list[i - first]

# temp에서 더 이동된 것을 원상복귀시킴
new_serial = temp_serial[-temp_start:] + temp_serial[:len(temp_serial)-temp_start]
first += temp_start
last += temp_start
if first > len(new_serial) or last > len(new_serial):
    first -= len(new_serial)
    last -= len(new_serial) 

total_pushed = num - new_serial.index(1)

try_num = 1
while True:
    first_push = try_num
    second_push = total_pushed - first_push
    if last + second_push + 1 > num:
        try_num += 1
        continue
    
    print(first_push)
    print("{} {}".format(first + second_push + 1, last + second_push + 1))
    print(total_pushed - first_push)
    break