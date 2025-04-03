# 문제 링크: https://www.acmicpc.net/problem/18352

from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)

q = deque([(x, 0)])
visited = {(x)}
destination = []

while q:
    city, dist = q.popleft()    

    for i in graph[city]:

        if not i in visited:            
            visited.add(i)            

            if dist + 1 == k:
                destination.append(i)
                continue
            else:
                q.append((i, dist+1))

if destination:    
    for i in sorted(destination):
        print(i)

else:
    print(-1)




        




