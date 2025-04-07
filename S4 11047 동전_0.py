# 문제 링크: https://www.acmicpc.net/problem/11047

import sys

# 입력 처리
input = sys.stdin.readline

n, goal = map(int, input().split())
coins = list(map(int, sys.stdin.read().splitlines()))

def getCoinN(array, goal):
    coins.reverse() # 최솟값을 구하기 위해 큰 동전부터 사용할 수 있도록 역정렬

    newGoal = goal # 총 목표 금액에서 남은 목표 금액
    current = 0 # 동전의 조합으로 만든 금액
    cnt = 0 # 조합에 사용된 동전 수
    
    for coin in coins:
        while coin <= newGoal:
            coinN = newGoal // coin # 빠른 계산을 위해 동전이 몇 개 필요한지 한 번에 계산
            newGoal -= coin * coinN
            current += coin * coinN
            cnt += coinN
        if current == goal:
            print(cnt)
            return

getCoinN(coins, goal)



