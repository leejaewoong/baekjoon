# 문제 링크: https://www.acmicpc.net/problem/1916

from collections import deque
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

cityN = int(input())
busN = int(input())
graph = [[] for i in range(cityN+1)]
for i in range(busN):
    dep, des, cost = map(int, input().split())
    graph[dep].append((des, cost))
start, end = map(int, input().split())

distance = [INF] * (cityN + 1)

def dijkstra(dep, des):
    global distance
    
    distance[dep] = 0
    q = []
    heapq.heappush(q, (0, dep))

    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue        

        for nextCity, weight in graph[now]:
            cost = weight + distance[now]
            if distance[nextCity] > cost:
                distance[nextCity] = cost
                heapq.heappush(q, (cost, nextCity))

    print(distance[des])

    
dijkstra(start, end)
            
            








