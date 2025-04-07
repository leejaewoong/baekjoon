# 문제 링크: https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 입력 처리

dp = [0] * (k+1) # 가방의 허용 무게별 최대 만족도를 저장할 리스트 생성

for idx in range(n):
    w, v = map(int, input().split()) # 아이템 입력 처리 후, 무게와 가치 출력
    
    for i in range(k, w-1, -1): # 가방의 허용 무게에서 주목 아이템의 무게까지 거꾸로 반복
        dp[i] = max(dp[i], dp[i-w] + v) # 주목 아이템을 취하는 것과 취하지 않는 것 중에 만족이 큰 값을 선택 

print(dp[k])

