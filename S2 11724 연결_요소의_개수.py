# 문제 링크: https://www.acmicpc.net/problem/11724

from collections import defaultdict
import sys
input = sys.stdin.readline

nodeN, edgeN = map(int, input().split())
graph = defaultdict(list)
for i in range(edgeN):
    key, value = map(int, input().split())
    graph[key].append(value)
    graph[value].append(key)

visited = [False] * (nodeN + 1)
count = 0

def dfs(start, visited):        
    visited[start] = True
    for k in graph[start]:
        if not visited[k]:
            dfs(k, visited)
    return visited

def getConnection(graph):
    global count, visited 
    for i in range(1, nodeN+1):        
        if not visited[i]:            
            if graph[i]:
                dfs(i, visited)
            count += 1
        
    print(count)

getConnection(graph)


