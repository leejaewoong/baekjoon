# 문제 링크: https://www.acmicpc.net/problem/2869

def getDate():
    data = list(map(int, input().split()))
    climb = data[0]
    slip = data[1]
    height = data[2]
    realHeight = height-slip
    realclimb = climb-slip
    if realHeight%realclimb == 0:
       date =  int(realHeight/realclimb)
       print(date)
    else:
        realDate = int(realHeight/realclimb+1)
        print(realDate)

getDate()