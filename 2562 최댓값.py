# 문제 링크: https://www.acmicpc.net/problem/2562

def getMax():
    numbers = []
    for i in range(9):
        number = int(input())        
        numbers.append(number)
    bigNumber = max(numbers)
    position = int(numbers.index(bigNumber)) + 1
    print(bigNumber)
    print(position) 

getMax()   

    

    