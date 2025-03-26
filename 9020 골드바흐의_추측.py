# 문제 링크: https://www.acmicpc.net/problem/9020

def isPrime(num):    
    prime = []
    for i in range(num):  # 소수 구하기                              
        for j in range(2, int(i ** 0.5)+1):
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime

def getCombi():    
    caseNumber = int(input())   
    numbers = [int(input()) for i in range(caseNumber)]  # 입력값 리스트로 저장

    prime = isPrime(max(numbers))
    for num in numbers:                
        for left in range(num//2, 1, -1):
            right = num-left
            if left in prime and right in prime:
                break
        print(left, right)

getCombi()


