# https://www.acmicpc.net/problem/1260
# list comprehension의 활용

from sys import stdin

def dfs(e):
    for num in range(edge):
        if matrix[e][num] == 1 and is_visited[num][0] == False:
            is_visited[num][0] = True
            print(num+1, end=' ')
            dfs(num)

def bfs(e):
    queue = [e]
    while len(queue) != 0:
        check = queue.pop(0)
        print(check+1, end=' ')
        for num in range(edge):
            if matrix[check][num] == 1 and is_visited[num][1] == False:
                is_visited[num][1] = True
                queue.append(num)

edge, vertex, start = map(int, stdin.readline().split())
start -= 1
matrix = [[0 for i in range(edge)] for j in range(edge)]
is_visited = [[False, False] for i in range(edge)]
is_visited[start] = [True, True]

for i in range(vertex):
    e1, e2 = map(int, stdin.readline().split())
    matrix[e1 - 1][e2 - 1] = 1
    matrix[e2 - 1][e1 - 1] = 1

print(start+1, end=' ')
dfs(start)
print()
bfs(start)