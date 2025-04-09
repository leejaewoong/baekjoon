

import sys
input = sys.stdin.readline
INF = int(1e9)

# 입력 처리
n = int(input())
tariff = [i for i in (list(map(int, input().split())) for j in range(n))]

minCosts = [] # 반복문을 돌며 매 출발도시의 minCost를 적재할 리스트 생성

def dfs(cur, cityN, cost):
    global minCost # minCost를 함수 안팎에서 쓰기 위한 전역 변수 선언

    if cityN == n: # 모든 도시를 방문하면 아래 연산 수행
        if tariff[cur][start]: # 마지막 도시에서 출발 도시로 가는 경로가 있다면 minCost를 계산
            minCost = min(minCost, cost + tariff[cur][start]) # 기존의 minCost와 현재 cost에서 출발 도시록 돌아갈 비용을 더한 값 중 최솟값 선택
        
    for next in range(n): # 다른 도시를 반복해서 탐색
        if next not in visited and tariff[cur][next]: # 방문하지 않은 도시이며, 비용이 0이 아닌 도시(현재 도시 또는, 경로가 없는 경우)에 한해서 아래 연산 수행
            visited.add(next) # 다음 도시 방문 처리
            dfs(next, cityN+1, cost+tariff[cur][next]) # 다음 도시, 방문 횟수+1, 누적 비용+다음 비용을 파라미터로 재귀함수 호출
            visited.remove(next) # 다른 조합을 위한 다음 도시 방문 처리 해제    

for start in range(n):
    visited = set()
    visited.add(start) # 함수 내에서 출발 도시를 방문하지 않도록 방문 처리
    minCost = INF
    dfs(start, 1, 0)
    minCosts.append(minCost) # 함수에서 연산한 minCost를 리스트에 삽입

print(min(minCosts))



