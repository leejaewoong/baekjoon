# 문제 링크: https://www.acmicpc.net/problem/2753

def getLeapYear ():            
    while True:
        try:
            year = int(input())                                                          
            if year%400 == 0:
                print(1)
            elif year%100 == 0:
                print(0)
            elif year%4 == 0:
                print(1)
            else:
                print(0)
        except EOFError:
            break

getLeapYear()

