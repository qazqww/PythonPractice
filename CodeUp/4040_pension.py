# https://codeup.kr/problem.php?id=4040

room_state = []

days, rooms = map(int, input().split())
for i in range(days):
    room_state.append(input())
arrive, leave = map(int, input().split())

arrive -= 1
leave -= 1
now = arrive
changed = -1

while now < leave:
    longest = -1
    for i in range(rooms):
        if room_state[now][i] == 'O':
            k = 1
            while now + k < leave and room_state[now + k][i] == 'O':
                k += 1
            if k > longest:
                longest = k

    if longest == -1:
        print(-1)
        exit()

    now += longest
    changed += 1

print(changed)