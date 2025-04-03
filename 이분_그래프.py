from collections import deque, defaultdict
import sys
input = sys.stdin.readline

caseN = int(input())
graph = defaultdict(list)

defaultdict(<class 'list'>, {1: [3], 2: [3]})
defaultdict(<class 'list'>, {1: [2], 2: [3], 3: [4], 4: [2]})

def isBiset():
    





for i in range(caseN):
    v, e = map(int, input().split())
    for i in range(e):
        key, value = map(int, input().split())
        graph[key].append(value)

    result = isBiset(graph)
    print(result)
    graph = defaultdict(list)








