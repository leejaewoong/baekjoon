# 문제 링크: https://www.acmicpc.net/problem/2606

import sys
input = sys.stdin.readline

computerN = int(input())
pairN = int(input())

parents = [i for i in range(computerN+1)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    if rootA != rootB:
        parents[rootB] = rootA
    
edge = [(com1, com2) for com1, com2 in (map(int, input().split()) for i in range(pairN))]

for a, b in edge:
    union(a, b)

def infectedComputerN(computerN):
    count = 0
    for i in range(2, computerN+1):        
        is_infected = find(i)
        if is_infected == find(1): # 1번 컴퓨터가 루트로 지정되지 않을 경우
            count += 1

    print(count)

infectedComputerN(computerN)








