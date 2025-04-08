# 문제 링크: https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

# 입력처리
n = int(input())
schedule = [[end, start] for start, end in (map(int, input().split()) for i in range(n))]
schedule.sort() # 회의들을 1. 마치는 시간 2. 시작 시간 순으로 정렬 / 시작하자마자 마치는 경우를 대비해 시작 시간을 2순위로 정렬

cnt = 0 # 회의 수를 세기 위한 변수 선언
next = 0 # 다음 회의의 시작 가능한 시간을 체크하기 위한 변수 선언

for meeting in schedule:
    if next <= meeting[1]: # 이전 회의 시간의 종료 시간 이후에 시작하는 회의인지 확인
        cnt += 1 
        next = meeting[0] # 다음 회의 시작 가능 시간 업데이트

print(cnt)



