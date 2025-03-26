# 문제 링크: https://www.acmicpc.net/problem/2630

import sys

input = sys.stdin.readline

N = int(input())
square = [list(map(int, input().split())) for i in range(N)]

countB = 0
countW = 0

def slice4(array, N): # 4등분 함수
    x1, x2, x3, x4 = [], [], [], []
    for i in range(N//2):
        x1.append(list(map(int, array[i][:N//2]))) #좌상단
        x2.append(list(map(int, array[i][N//2:]))) #우상단
        x3.append(list(map(int, array[i+(N//2)][:N//2]))) #좌하단
        x4.append(list(map(int, array[i+(N//2)][N//2:]))) #우하단
    return x1, x2, x3, x4

def getScore(array): # 리스트의 총점 확인 함수
    score = sum(sum(row) for row in array)    
    return score

def getPaperN(array, N): # 컬러별 색종이 개수 구하기
    global countW, countB 

    score = getScore(array)        
    if score == N *N: # 색종이가 모두 파란색이면
        countB += 1
        return
    elif score == 0: # 색종이가 모두 흰색이면
        countW += 1
        return    
    else:             
        for x in slice4(array, N):                    
            getPaperN(x, N//2) # 다시 4등분해서 점수에 따라 색종이 수 카운트
   
getPaperN(square, N)
print(countW)
print(countB)




        







