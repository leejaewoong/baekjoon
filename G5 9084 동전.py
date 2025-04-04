# 문제 링크: https://www.acmicpc.net/problem/9084

from collections import deque
import sys
input = sys.stdin.readline

# 입력 처리
T = int(input())

for test in range(T):
    coinN = int(input())
    coins = list(map(int, input().split()))
    goal = int(input())

    ## DP: bottom-up으로 해결

    dp = [0] * (goal + 1) # 목표 금액별 가능한 조합의 수를 저장하기 위한 리스트 생성
    
    dp[0] = 1 # 목표 금액 0을 만들기 위한 방법(아무 것도 조합하지 않기)으로 1을 정의

    if goal > 0:
        for coin in coins:
            for i in range(coin, goal+1):
                dp[i] += dp[i-coin] # 동전별로 조합의 수를 더하여 누적

    print(dp[goal])    


    ## BFS으로 해결
    comb = {coin:0 for coin in coins} # 순서 상관없이 사용된 코인 수로 경우의 수 확인
    q = deque([(comb, goal)]) # 갱신될 조합과 목표 금액을 삽입
    cnt = 0 # 조합의 수 확인용 변수
    completedComb = set() # 조합의 중복을 확인할 set    

    while q:
        newComb, newGoal = q.popleft() # 큐에서 갱신한 조합과 목표 금액 출력        

        for coin in coins:
            eachGoal = newGoal - coin # 코인별로 새로운 목표 금액을 연산할 수 있게 새로운 변수 정의
            eachComb = newComb.copy() # 코인별로 새로운 조합을 저장할 수 있게 새로운 변수 정의
            eachComb[coin] += 1 # 사용된 코인의 수만 증가
            key = tuple(sorted(eachComb.items())) # 조합을 해시 가능한 형태로 변환
        
            if eachGoal == 0 and key not in completedComb: # 목표 금액에 딱 맞는 조합이면서 중복이지 않은 경우만 카운트
                completedComb.add(key)
                cnt += 1

            elif eachGoal > 0: # 목표 금액까지 동전의 조합이 더 필요한 경우 현재까지의 조합과 목표를 큐에 삽입
                q.append((eachComb, eachGoal))

    print(cnt)







        
# %%
