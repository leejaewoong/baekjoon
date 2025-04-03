# 문제 링크: https://www.acmicpc.net/problem/11053

from bisect import bisect_left
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
target = list(map(int, input().split()))
temp = deque()

for i in range(len(target)):
    if not temp: 
        temp.append(target[i])
        continue

    elif temp[-1] < target[i]:
        temp.append(target[i])
        continue
    
    else:
        idx = bisect_left(temp, target[i])
        temp[idx] = target[i]
        continue

ans = len(temp)

print(ans)
