# 문제 링크: https://www.acmicpc.net/problem/1085

x,y,w,h = map(int, input().split())
moveUp = h-y
moveDown = y
moveRight = w-x
moveLeft = x
move = [moveUp, moveDown, moveRight, moveLeft]
answer = min(move)
print(answer)


