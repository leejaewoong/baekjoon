# 문제 링크: https://www.acmicpc.net/problem/10773

import sys
input = sys.stdin.readline

k = int(input())
account = []

def getAccount():    
    for cmd in range(k):
        cmd = int(input())
        if cmd:
            account.append(cmd)                
        else:
            if account:
               account.pop()                                 
            else:
               continue
    
    print(sum(account))

getAccount()
                