# 문제 링크: https://www.acmicpc.net/problem/10872

def getFactorial():
    number = int(input())
    if number == 0:
        print(1)
    else:
        list = []        
        for i in range(1, number+1):
            list.append(i)
        answer = 1
        for j in list:
            answer *= j
        print(answer)

getFactorial()
    