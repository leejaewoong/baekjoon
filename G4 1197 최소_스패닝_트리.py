# 문제 링크: https://www.acmicpc.net/problem/1197

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e = map(int, input().split())
originalGraph = sorted([[cost, a, b] for a, b, cost in (map(int, input().split()) for i in range(e))])

parent = [i for i in range(v+1)]

def findGroup(a):
    if parent[a] != a:
        parent[a] = findGroup(parent[a])
    return parent[a]

def isSameGroup(a, b):
    return findGroup(a) == findGroup(b)       
    
def union(a, b):
    rootA = findGroup(a)
    rootB = findGroup(b)
    if rootA != rootB:
        parent[rootA] = rootB
    return parent[rootA]
         
def getMst(array):
    global v    
    graph = []       
    
    for i in array:            
        a = i[1]
        b = i[2]
        if not isSameGroup(a, b):
            graph.append(i)
            union(a, b)

    weight = 0

    for i in graph:
        weight += i[0]

    return weight

result = getMst(originalGraph)
print(result)



                



    