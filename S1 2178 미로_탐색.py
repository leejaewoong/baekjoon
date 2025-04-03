# 문제 링크: https://www.acmicpc.net/problem/2178

from collections import deque, defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rawMaze = [input().strip() for i in (j for j in range(N))]
maze = {(x, y): int(rawMaze[x][y]) for x in range(N) for y in range(M)}

q = deque([((0, 0), 1)])
visited = {(0, 0)}

dx = [1, -1 , 0, 0]
dy = [0, 0, 1, -1]

while q:
    (nx, ny), dist = q.popleft()

    if nx == N-1 and ny == M-1:
        print(dist)
        exit()

    for i in range(4):
        moveX = nx + dx[i]
        moveY = ny + dy[i]

        if 0 <= moveX < N and 0 <= moveY < M and maze[(moveX, moveY)] == 1 and not (moveX, moveY) in visited:
            q.append(((moveX, moveY), dist + 1))
            visited.add((moveX, moveY))


# 시간초과 코드

# for x in range(N):
#     for y in range(M):
#         v = int(rawMaze[x][y])
#         maze.append([x,y,v])    

# visited = [False] * len(maze)
# q = deque()
# start = maze[0]
# visited[0] = True
# q.append([start, 1])

# while q:        
#     pos, dist = q.popleft()
#     p = maze.index(pos)    
#     up = maze[p - M] if p - M >= 0 else None
#     down = maze[p + M] if p + M < len(maze) else None
#     right = maze[p+1] if (p+1) % M != 0 else None
#     left = maze[p-1] if (p)  % M != 0 else None

#     direction = [d for d in [up, down, right, left] if d != None]

#     for i in direction: 
#         if i in maze and i[2] == 1 and not visited[maze.index(i)]:            
#             visited[maze.index(i)] = True                      
#             q.append([i, dist + 1])            

#             if i[0] == N-1 and i[1] == M-1:                
#                 dist += 1
#                 print(dist)
#                 exit()

