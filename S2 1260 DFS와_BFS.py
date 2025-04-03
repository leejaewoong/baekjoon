# 문제 링크: https://www.acmicpc.net/problem/1260

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

nodeN, edgeN, start = map(int, input().split())

graph = defaultdict(list)
for i in range(edgeN):
    key, value = map(int, input().split())
    graph[key].append(value)
    graph[value].append(key)

visited = [False] * (nodeN + 1)
result = []

def dfs(graph, start): # dfs로 구하기    
    visited[start] = True
    result.append(start)    

    for i in sorted(graph[start]):
        if not visited[i]:
            dfs(graph, i)

    return result


def bfs(graph, start): # bfs로 구하기
    travel = deque([start])
    visited[start] = True

    while travel:        
        v = travel.popleft()
        result.append(v)        
        for i in sorted(graph[v]):
            if not visited[i]:
                travel.append(i)
                visited[i] = True

    return result

dfs(graph, start)
print(*result)

visited = [False] * (nodeN + 1)
result = []

bfs(graph, start)
print(*result)



    



    