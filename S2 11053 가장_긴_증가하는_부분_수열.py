from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
array = [i for i in list(map(int, input().split()))]


# 재귀 함수로 해결
def getLis(prev, next): 
    if next == len(array):
        return 0
    
    skip = getLis(prev, next+1)

    take = 0
    if prev == -1 or array[prev] < array[next]:
        take = getLis(next, next+1) + 1

    return max(skip, take)

print(getLis(-1,0))


# DP: bottom-up으로 해결
dp = [1] * (n)

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


# 이분탐색 기반의 그리디 + DP로 해결
result = [array[0]]

for j in array:
    i = result[-1]

    if i < j:
        result.append(j)
    elif i > j:        
        result[bisect_left(result, j)] = j

print(len(result))

