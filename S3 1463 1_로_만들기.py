# 문제 링크: https://www.acmicpc.net/problem/1463

from collections import deque
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())


# BFS로 해결
visited = set() # 탐색 속도를 높이기 위해 set 사용
q = deque()
q.append([n, 0]) # 입력 받은 n과 연산 횟수(0)을 q에 삽입

while q:
    num, cnt = q.popleft() # q에서 연산할 숫자와 연산 횟수를 꺼냄    

    if num == 1: # 먼저 1이 되는 연산식이 있으면 출력하고 함수 종료
        print(cnt) 
        break
    
    if num in visited: # 꺼낸 숫자를 처리한 적이 있다면 skip!
        continue    
    visited.add(num) # 꺼낸 숫자 방문 처리

    if num % 3 == 0: 
        q.append([num // 3, cnt+1])            
    if num % 2 == 0: # 3과 2 모두 나눠지는 경우를 대비해 if로 작성
        q.append([num // 2, cnt+1])    
    q.append([num - 1, cnt+1])
    

# DP: bottom_up으로 해결

# n까지 이르는 수의 최소 연산 횟수를 저장할 리스트 생성 
# 아래에서 dp[i] = dp[i-1] + 1로 정의하기 때문에 0도 기본값으로 충분 
# 자연스럽게 연산이 필요없는 dp[1]도 0으로 지정
dp = [0] * (n + 1) 

for i in range(2, n+1):       
    dp[i] = dp[i-1] + 1 # case 1. dp[i]는 1을 뺀 i-1보다 최소한 한 번의 연산을 더 함

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1) # case 2. dp[i]는 1를 3으로 나눈 i//3보다 최소한 한 번의 연산을 더 함 (더 작은 값으로 반환)

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1) # case 3. dp[i]는 1를 2으로 나눈 i//2보다 최소한 한 번의 연산을 더 함 (더 작은 값으로 반환)

print(dp[n])


# DFS로 해결
def dfs(n):
    if n == 1: # n이 1일 때는 연산이 필요없기 때문에 0으로 정의
        return 0 
    
    calN = dfs(n - 1) + 1 # case 1. n에서 1을 뺀 n-1보다 최소한 한 번의 연산을 더 함

    if n % 3 == 0:
        calN = min(calN, dfs(n // 3) + 1) # case 2. n를 3으로 나눈 i//3보다 최소한 한 번의 연산을 더 함 (더 작은 값으로 반환)

    if n % 2 == 0:
        calN = min(calN, dfs(n // 2) + 1) # case 3. n를 3으로 나눈 i//3보다 최소한 한 번의 연산을 더 함 (더 작은 값으로 반환)
    
    return calN

print(dfs(n))


# DP: top_down으로 해결

# n까지 이르는 수의 최소 연산 횟수를 저장할 리스트 생성 
# 아래에서 memo[n]과 항상 비교하여 최소값을 저장하기 때문에 무한대 값으로 정의
memo = [int(1e9)] * (n+1) 
memo[1] = 0  # 재귀함수에서 반복적으로 선언되는 것을 방지하기 위해 밖에서 정의

def makeOne(n):

    if memo[n] != int(1e9): # memo[n] 값이 있으면 연산하지 않고 그대로 반환 
        return memo[n]    

    if n > 1:
    
        memo[n] = makeOne(n-1) + 1 # case 1. dp[n]는 1을 뺀 n-1보다 최소한 한 번의 연산을 더 함

        if n % 3 == 0:
            memo[n] = min(memo[n], makeOne(n//3)+1) # case 2. dp[n]는 1를 3으로 나눈 n//3보다 최소한 한 번의 연산을 더 함 (더 작은 값으로 반환)        

        if n % 2 == 0:
            memo[n] = min(memo[n], makeOne(n//2)+1) # case 3. dp[n]는 1를 2으로 나눈 n//2보다 최소한 한 번의 연산을 더 함 (더 작은 값으로 반환)

    return memo[n]

print(makeOne(n))

    







