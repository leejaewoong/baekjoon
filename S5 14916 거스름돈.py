# 문제 링크: https://www.acmicpc.net/problem/14916

from collections import deque
import sys
input = sys.stdin.readline

changes = int(input()) # 거스름돈 입력 처리

cnt = 0 # 동전 수를 헤아릴 변수 선언

# 일반 식으로 해결
while True:
    # 남은 거스름돈이 5의 배수이면 5로 나눈 몫을 더해서 동전 수 출력
    if changes % 5 == 0: 
        cnt += changes // 5
        print(cnt)
        exit()

    # 남은 거스름돈이 2의 배수가 아니라면 잔액에서 2를 빼고 동전 수를 +1
    else:
        changes -= 2
        cnt += 1

        # 남은 거스름돈이 0이면 동전 수 출력 후 종료
        if changes == 0:
            print(cnt)
            exit()

        # 남은 거스름돈이 2 미만이면 -1 출력 후 종료
        elif changes < 2:
            print(-1)
            exit()


# BFS로 해결
coins = [5, 2] # 반복문에서 꺼낼 동전 리스트 생성

q = deque() 
q.append((changes, cnt)) 
visited = set()

while q:
    changes, cnt = q.popleft() # 큐에서 남은 거스름돈과 동전 수를 출력

    if changes in visited: # 남은 거스름돈이 연산된 적이 있다면 건너뛰기
        continue

    visited.add(changes) # 현재 남은 거스름돈을 기록 처리

    for coin in coins: # 5원부터 순차적으로 연산 수행

        restChanges = changes - coin # 동전 금액을 뺀 남은 거스름돈을 갱신                                              

        if restChanges == 0: # 남은 거스름돈이 0이라면 동전 수를 출력하고 종료
            print(cnt+1)
            exit()

        if restChanges > 0: # 남은 거스름돈이 0원 이상일 때만 큐에 남은 거스름돈과 동전 수를 +1한 값을 삽입
            q.append((restChanges, cnt+1))         

print(-1) # 반복문이 종료될 때까지 남은 거스름돈이 0이 될 경우를 찾지 못한다면 -1을 출력하고 종료

