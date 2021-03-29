# https://www.acmicpc.net/problem/2309

height = []
for i in range(9):
    height.append(int(input()))

sum_height = sum(height)
for i in range(8):
    for j in range(i+1, 9):
        if sum_height - (height[i] + height[j]) == 100:
            del(height[j], height[i])
            height.sort()
            for k in height:
                print(k)
            exit()