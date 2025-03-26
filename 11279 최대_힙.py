# 문제 링크: https://www.acmicpc.net/problem/11279

import heapq
import sys

input = sys.stdin.readline

N = int(input())
input = [int(input()) for i in range(N)]

array = []

for j in input:
    if j == 0:
        if not array:
            print(0)            
        else:
            print(-heapq.heappop(array))            
    else:
        heapq.heappush(array, -j)






