# 문제 링크: https://www.acmicpc.net/problem/2750  

def mySort():
    tryNumber = int(input()) 
    numbers = []
    for i in range(tryNumber):
        num = int(input())
        numbers.append(num)
    numbers.sort()
    for i in numbers:
        print(i)

mySort()
    

