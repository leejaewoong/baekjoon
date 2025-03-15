# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

def sumNumbers():
    caseNumber = int(input())
    for i in range(caseNumber):
        numbers = list(map(int, input().split()))
        result = sum(numbers)
        print(result)

sumNumbers()        

