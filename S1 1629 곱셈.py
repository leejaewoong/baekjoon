# 문제 링크: https://www.acmicpc.net/problem/1629

import sys
input = sys.stdin.readline

# a, b, c = map(int, input().split())
a, b, c = 10, 11, 12

origin = a
cnt = 1

if b > 1:        
    while cnt*2 <= b:
        a *= a 
        a % c
        cnt *= 2

if b == 1 or b - cnt == 0: 
    result = a % c

else:    
    for i in range(b-cnt):
        a *= origin
    result = a % c    

print(result)