# https://codeup.kr/problem.php?id=2601

N = int(input())

if N == 1 or N == 2:
    print("1")

else:
    num1, num2 = 1, 1
    
    for i in range(N-2):
        temp = num2
        num2 = num1 + num2
        num1 = temp
    
    print(num2)