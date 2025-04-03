# 문제 링크: https://www.acmicpc.net/problem/11404

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for i in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    dep, des, cost = map(int, input().split())
    graph[dep][des] = min(graph[dep][des], cost)

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
 
for i in range(n+1):
    for j in range(n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(1, n+1):
    print(*graph[i][1:])



