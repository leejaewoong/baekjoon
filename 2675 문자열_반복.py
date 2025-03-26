# 문제 링크: https://www.acmicpc.net/problem/2675

def rep():
    caseNumber = int(input())    
    for case in range(caseNumber):
        data = input().split()
        r = int(data[0])
        text = data[1]
        fullText = ""
        for i in text:
            partText = i*r
            fullText += partText
        print(fullText)

rep()
        


