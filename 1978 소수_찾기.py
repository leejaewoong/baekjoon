# 문제 링크: https://www.acmicpc.net/problem/1978

def getPrime():
    tryNumber = int(input())
    numbers = list(map(int, input().split()))
    prime = []
    for num in numbers:        
        if num < 2:
            continue                
        for i in range(2, num):
            if num % i == 0:
                break                 
        else: prime.append(num)        
    print(len(prime))

getPrime()
