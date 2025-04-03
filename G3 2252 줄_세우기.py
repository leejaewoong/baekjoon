# 문제 링크: https://www.acmicpc.net/problem/2252

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def toplogy():
    graph = [[] for i  in range(n + 1)]
    indegree = [0 for i in range(n + 1)]
    q = deque()
    result = []

    for i in range(m):
        smaller, taller = map(int, input().split())
        graph[smaller].append(taller)
        indegree[taller] += 1

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)            

    while q:
        student = q.popleft()
        result.append(student)        
        for i in graph[student]:
            indegree[i] -= 1
            if indegree[i] == 0:                
                q.append(i)                

    print(*result) 

toplogy()
