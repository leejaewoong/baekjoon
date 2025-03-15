# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

def drawStars():
    number = int(input())
    for i in range(number):
        print("*"*(i+1))

drawStars()

