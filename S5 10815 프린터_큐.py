# 문제 링크: https://www.acmicpc.net/problem/1966

from collections import deque
import sys
input = sys.stdin.readline

def printOrder(array, target):    
    
    output = 0    

    while True:

        if max(array, key=lambda x: x[0]) != array[0]:
            array.rotate(-1)            

        else:
            if array[0][1] == True:
                array.popleft()            
                output += 1
                break
            else:
                array.popleft()            
                output += 1

    print(output)

testN = int(input())

for i in range(testN):
    docN, targetDoc = map(int, input().split())
    docs = deque((priority, idx == targetDoc) for idx, priority in enumerate(map(int, input().split())))
    printOrder(docs, targetDoc)


