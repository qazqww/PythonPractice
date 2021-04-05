# https://www.acmicpc.net/problem/3460

T = int(input())
for _ in range(T):
    binary = bin(int(input()))[2:]
    for i in range(len(binary)):        
        if binary[len(binary) - i - 1] == '1':
            print(i, end=' ')