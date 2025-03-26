# 문제 링크: https://www.acmicpc.net/problem/2628

def getArea():
    square = list(map(int, input().split()))
    h = square[0] # 가로 길이
    v = square[1] # 세로 길이
    hor = [0, v] # 가로로 자른 지점
    ver = [0, h] # 세로로 자른 지점
    slices = int(input()) # 자르는 수    
    for slice in range(slices):
        slice = list(map(int, input().split())) # 자른 지점 입력
        if slice[0] == 1:
            ver.append(slice[1])
        else:
            hor.append(slice[1])
    ver.sort()
    hor.sort()
    verDiff = []
    horDiff = []
    for i in range(1, len(ver)):                
        diff = ver[i] - ver[i-1]
        verDiff.append(diff)
    for i in range(1, len(hor)):                
        diff = hor[i] - hor[i-1]
        horDiff.append(diff)
    maxArea = max(horDiff)*max(verDiff)
    print(maxArea)

getArea()

        

        
            
