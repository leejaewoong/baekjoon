# 문제 링크: https://www.acmicpc.net/problem/11866

from collections import deque
import sys

input = sys.stdin.readline

N, D = map(int, input().split())
# N = 7
# D = 3
list = deque(i+1 for i in range(N))

ans = []

while len(list):
    for i in range(D-1):        
        list.append(list.popleft())                   
    ans.append(list.popleft())
    
print("<" + ", ".join(map(str, ans)) + ">")



    







