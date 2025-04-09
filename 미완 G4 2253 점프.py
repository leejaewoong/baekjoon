# 문제 링크: https://www.acmicpc.net/problem/2253

from collections import deque
import sys
input = sys.stdin.readline

# 입력 처리
n, m = map(int, input().split())
notAvailable = [int(i) for i in sys.stdin.read().splitlines()]


# 시간 초과 (BFS)
q = deque() 
q.append([2, 1, 1]) # 큐에 현재 돌 위치, 누적 점프 횟수, 점프 거리를 삽입
visited = set()

while q:
    idx, jump, stride = q.popleft() # 큐에서 현재 돌 위치, 누적 점프 횟수, 점프 거리를 출력

    if (idx, stride) not in visited: # 현재 돌 위치와 점프 거리가 연산된 적 없을 때만 연산 수행
        visited.add((idx, stride)) # 현재 돌 위치와 점프 거리 연산 기록 추가

        comb = [stride + 1, stride, stride - 1] # 가능한 점프 거리를 원소로 리스트 생성

        for i in comb:
            if idx + i not in notAvailable and i > 0: # 최소 1칸 이상을 점프하여 착지 가능한 돌에 다다랄 경우만 아래 연산 수행
                newIdx = idx + i # 새로 착지한 곳은 도약한 돌에서 점프 거리를 더한 위치로 선언
                if newIdx >= n: # 새로 착지한 곳이 도착지거나 이후의 돌이라면, 점프 횟수 출력 후 종료
                    print(jump+1)
                    exit()
            q.append([newIdx, jump+1, i]) # 새로 착지한 돌과 1회 추가한 점프 횟수, 점프 거리를 큐에 삽입                





