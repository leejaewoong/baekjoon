# 문제 링크: https://www.acmicpc.net/problem/2493

from collections import deque
import sys

def getReceiver():
    N = int(sys.stdin.readline())    
    height = list(map(int, sys.stdin.readline().split()))

    towers = deque()
    for i in range(N):
        tower = [i, height[i]]
        towers.append(tower)
    
    # towers.appendleft([0,0])
    temp = []
    receivers = []    

    for i in range(N):       
        
        received = False  

        while temp:
            if towers[i][1] > temp[-1][1]:
                temp.pop()
            else:
                receivers.append(temp[-1][0]+1)
                received = True
                break

        if not received:
            receivers.append(0)

        temp.append(towers[i])
             
    print(*receivers)
            
getReceiver()   

    
    