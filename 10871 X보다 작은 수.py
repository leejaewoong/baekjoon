# 문제 링크: https://www.acmicpc.net/problem/10871

def getSmallerX():
    n, x = map(int, input().split())
    numbers = list(map(int, input().split()))
    answer = [i for i in numbers if i < x]    
    print(*answer)

getSmallerX()

