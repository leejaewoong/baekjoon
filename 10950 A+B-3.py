# 문제 링크: https://www.acmicpc.net/problem/10950

def sumNumbers():
    caseNumber = int(input())
    for i in range(caseNumber):
        numbers = list(map(int, input().split()))
        result = sum(numbers)
        print(result)

sumNumbers()        

