# 문제 링크: https://www.acmicpc.net/problem/9251

import sys
input = sys.stdin.readline

# 입력 처리
str1 = input().strip()
str2 = input().strip()


# DP: bottom_up으로 해결
dp = [[0] * (len(str2)+1) for i in range((len(str1))+1)] #dp에 str1과 str2의 길이에 맞춰 2차원 리스트 생성 (이전 인덱스의 값을 참조하여 누적하기 때문에 길이에 +1)

# 생성한 2차원 리스트의 모든 행렬을 반복 (이전 인덱스의 값을 참조하여 누적하기 때문에 길이에 +1)
for i in range(1, (len(str1)+1)): 
    for j in range(1, (len(str2)+1)):
        if str1[i-1] == str2[j-1]: # 문자가 같다면 이전 인덱스의 리스트의 값에 +1
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 문자가 다르다면 str1과 str2의 각 이전 인덱스의 값 중에 최대값을 계승
print(dp[-1][-1])


# DP: top_down으로 해결
memo = {} # 연산값을 저장할 메모 dict 생성

def dp(i:int, j:int):
    if (i, j) in memo: # 메모에 해당 인덱스를 키로 하는 데이터가 있다면, 기존 연산값 반환
        return memo[(i, j)]
    
    if i == len(str1) or j == len(str2): # 어떤 문자열이라도 마지막 인덱스를 넘어서면 비교 종료
        return 0
    elif str1[i] == str2[j]: # 문자가 같다면 1을 더하여 두 문자열 모두 다음 인덱스를 비교
        memo[(i, j)] = dp(i+1, j+1) + 1
    else:
        memo[(i, j)] = max(dp(i, j+1), dp(i+1, j)) # 문자가 다르면 각 문자열의 다음 인덱스를 비교하는 2가지 케이스 중 최대값을 반환
    return memo[(i, j)] # 연산값을 해당 인덱스에 반환

print(dp(0, 0))


# DP: top_down으로 해결 (캐쉬 데코레이터 활용)
from functools import cache # 캐쉬 데코레이터 불러오기
@cache
def dp(i:int, j:int):
    if i == len(str1) or j == len(str2): # 어떤 문자열이라도 마지막 인덱스를 넘어서면 비교 종료
        return 0
    if str1[i] == str2[j]: # 문자가 같다면 1을 더하여 두 문자열 모두 다음 인덱스를 비교
        return dp(i+1, j+1) + 1
    else:
        return max(dp(i+1, j), dp(i, j+1)) # 문자가 다르면 각 문자열의 다음 인덱스를 비교하는 2가지 케이스 중 최대값을 반환
    
print(dp(0, 0))