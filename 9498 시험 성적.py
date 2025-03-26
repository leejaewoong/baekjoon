# 문제 링크: https://www.acmicpc.net/problem/9498

def getGrade():
    score = int(input())
    if score > 89:
        print ('A')
    elif score < 90 and score > 79:
        print ('B')
    elif score < 80 and score > 69:
        print ('C')
    elif score < 70 and score > 59:
        print ('D')
    else:
        print ('F')                        

getGrade()

