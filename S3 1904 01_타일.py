# 문제 링크: https://www.acmicpc.net/problem/1904

import sys
input = sys.stdin.readline

# 입력 처리
n = int(input()) 


# DP로 해결
dp = [0] * (n + 1) # n에 따른 조합의 수를 저장할 리스트 생성

dp[0] = 1 # 피보나치 수열에 따라 0, 1에 1 삽입
dp[1] = 1

for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746 # 점화식에 중간값에 15746을 나눠서 최종값에 너무 큰 수가 들어가지 않게 조절

print(dp[n])


# 리스트 없이 해결
a, b = 1, 1
for i in range(2, n + 1):
    a, b = b, (a + b) % 15746 # dp[c] = dp[a:(c-1)] + dp[b:(c-2)]를 활용하여 dp[a], dp[b] = dp[b] + dp[c:(a+b)]순으로 반복 진행 처리
print(b)