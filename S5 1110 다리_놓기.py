# 문제 링크: https://www.acmicpc.net/problem/1110

import sys
input = sys.stdin.readline

# 입력 처리
t = int(input())

memo = [[0] * 31 for i in range(31)] # 두 개의 파라미터에 따른 값을 저장하기 위해 2차원 리스트를 제작 (최대 입력값으로 설정)

def caseN(m, n):
    if m == n or n == 0: # 파스칼 공식에 따른 값 반환
        return 1    

    if memo[m][n] != 0: # 기본 값이 아닐 경우, 이미 연산한 값이 저장되어 있다는 의미
        return memo[m][n]

    memo[m][n] = caseN(m-1, n-1) + caseN(m-1, n) # 계산한 적이 없는 경우에만 파스칼 공식에 따라 계산한 값을 memo에 저장
    return memo[m][n]

# 테스트 수에 맞춰 함수 호출
for i in range(t):
    n, m = map(int, input().split())
    result = caseN(m, n)
    print(result)

    


