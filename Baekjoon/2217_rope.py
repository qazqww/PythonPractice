# https://www.acmicpc.net/problem/2217

from sys import stdin

num = int(input())
rope_list = []
for i in range(num):
    rope_list.append(int(stdin.readline()))

rope_list.sort(reverse=True)
used_rope, temp_rope = [rope_list[0]], [rope_list[0]]
now = 0

for i in range(1, len(rope_list)):
    temp_rope.append(rope_list[i])
    if rope_list[i] * len(temp_rope) >= used_rope[len(used_rope) - 1] * len(used_rope):
        used_rope += rope_list[now + 1:i + 1]
        now = i

print(min(used_rope) * len(used_rope))