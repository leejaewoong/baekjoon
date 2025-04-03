# 문제 링크: https://www.acmicpc.net/problem/2637

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
indegree = [0 for i in range(n+1)]
graph = [[] for i in range(n+1)]
need = [0 for i in range(n+1)]
q = []
notBasic = set()

for i in range(m):
    bigger, smaller, amount = map(int, input().split())
    graph[bigger].append((smaller, amount))
    indegree[smaller] += 1 
    notBasic.add(bigger)

q = deque([(n, 1)])

while q:
    module, vol = q.popleft()    
    for part, amount in graph[module]:           
        need[part] += vol * amount
        indegree[part] -= 1
        if indegree[part] == 0:
            q.append((part, need[part]))

for i in range(1, n+1):
    if i not in notBasic:
        print(i, need[i])         
 