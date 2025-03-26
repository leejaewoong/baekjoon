# 문제 링크: https://www.acmicpc.net/problem/2908

def answer():
    problem = input().split()
    numbers = []
    for i in problem:
        i = list(i)        
        i = i[::-1]
        num = ''
        for x in range(len(i)):
            num += i[x]
            numbers.append(num)
        numbers = list(map(int, numbers))
    ans = max(numbers)
    print(ans)

answer()
        
        
