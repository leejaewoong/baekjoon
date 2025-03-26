# 문제 링크: https://www.acmicpc.net/problem/9012

import sys

input = sys.stdin.readline
ctn = 0
testNumber = int(input())

def vaildVPS():    
    global ctn
    for case in range(testNumber):
        case = list(input())        
        for idx in range(len(case)-1):
            if case[idx] == '(':
                ctn += 1                                
            else:
                ctn -= 1                
            if ctn < 0:
                print('NO')
                break
        else:            
            if ctn == 0:
                print('YES')
            else:
                print('NO')
        ctn = 0

vaildVPS()