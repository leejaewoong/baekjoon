# 문제 링크: https://www.acmicpc.net/problem/1991

import sys
input = sys.stdin.readline

N = int(input())
nodes = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_result = -float('inf')
min_result = float('inf')

def dfs(idx, current):     
    global max_result, min_result

    if idx == N:
        max_result = max(max_result, current)
        min_result = min(min_result, current)
        return
    
    for i in range(4):
        if operators[i]:
            operators[i] -= 1
            if i == 0:
                dfs(idx + 1, current + nodes[idx])
            elif i == 1:
                dfs(idx + 1, current - nodes[idx])
            elif i == 2:
                dfs(idx + 1, current * nodes[idx])
            elif i == 3:
                if current < 0:
                    dfs(idx + 1, -(-current // nodes[idx]))
                else:
                    dfs(idx + 1, current // nodes[idx])
            operators[i] += 1
        
dfs(1, nodes[0])
print(max_result)
print(min_result)
      

