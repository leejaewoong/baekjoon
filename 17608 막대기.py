# 문제 링크: https://www.acmicpc.net/problem/17608

import sys

input = sys.stdin.readline

stickN = int(input())
sticks = []
for stick in range(stickN):
    stick = int(input())
    sticks.append(stick)

def visibleStick(array):    
    ctn = 0
    std = 0
    limit = sticks.index(max(sticks)) 

    for idx in range(len(sticks)-1, limit-1, -1):
        value = sticks[idx]        
        if value > std:
            std = value
            ctn += 1
        elif value <= std:
            continue
        else:        
            break

    print(ctn)

visibleStick(sticks)




