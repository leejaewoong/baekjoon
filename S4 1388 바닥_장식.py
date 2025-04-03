# 문제 링크: https://www.acmicpc.net/problem/1388

from collections import deque
import sys
input = sys.stdin.readline
graph = []

n, m = map(int, input().split())
floor = [i for i in (input().strip() for j in range(n))]
visited = [[False] * m for i in range(n)]
q = deque()

for x in range(n):
    for y in range(m):
        graph.append([x, y, floor[x][y]])

cnt = 0

for area in graph:
    
    x, y, z = area
    if visited[x][y]: 
        continue

    q.append(area)     
    visited[x][y] = True
    cnt += 1

    while q:
        x, y, z = q.popleft()        
        idx = (x * m) + y                

        if z == '-':            
            if y+1 < m and not visited[x][y+1] and graph[idx+1][2] == '-':
                q.append(graph[idx+1])
                visited[x][y+1] = True                

        if z == '|':
            if x+1 < n and not visited[x+1][y] and graph[idx+m][2] == '|':
                q.append(graph[idx+m])
                visited[x+1][y] = True                                        

print(cnt)








        











# %%
