# 문제 링크: https://www.acmicpc.net/problem/2748

import sys
input = sys.stdin.readline

# 입력 처리
n = int(input())

# 재귀함수 이용 (비효율)
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    result = fibo(n-1) + fibo(n-2)

    return result # return하지 않으면 호출된 재귀함수에서 None 값 반환


# bottom-up 방식
def fibo_dp(n):
    dp = [0] * (n+1) # 인덱스 에러가 나지 않도록 미리 초기값 설정
    
    dp[0] = 0
    dp[1] = 1        

    if n > 1: 
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2] # 2부터는 계산식을 통해 n까지의 답을 리스트에 저장 (n번만 계산)

    return dp[n]


memo = [-1] * (n+1) # 이미 계산한 적이 있는지 체크하기 위해 초기값 설정 (값으로 사용될 자연수 제외 / 함수 내부에서 선언 시 매번 새롭게 생성될 수 있기에 전역 리스트로 설정)    

# top-down 방식
def fibo_dp(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if memo[n] != -1: # 초기값 외에 다른 값이 저장되어 있다는 것은 계산하여 메모에 저장해두었다는 의미
        return memo[n]
    
    memo[n] = fibo_dp(n-1) + fibo_dp(n-2) # 계산한 적이 없는 경우에만 직접 계산한 결과를 리스트에 저장 (추후 중복 계산 방지)

    return memo[n]


# 함수 호출
result = fibo_dp(n)
print(result)





