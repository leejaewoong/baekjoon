# 문제 링크: https://www.acmicpc.net/problem/11725

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

nodeN = int(input())
graph = defaultdict(list)

for i in range(nodeN-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
visited = defaultdict(list)
visited[1].append(1)

while q:
    node = q.popleft()
    for i in graph[node]:
        if i not in visited:
            q.append((i))
            visited[i].append(node)

for k in range(2, len(visited)+1):
     print(*visited[k])
            
