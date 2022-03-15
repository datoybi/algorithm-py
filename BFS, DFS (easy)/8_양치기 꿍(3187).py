from collections import deque

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]
visited = [[False]*c for _ in range(r)]

def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    sheep, wolf = 0, 0
    while queue:
        i, j = queue.popleft()
        if graph[i][j] == 'k': # 양이면
            sheep += 1
        elif graph[i][j] == 'v': # 늑대면
            wolf += 1
        graph[i][j] = '#'
        for k in range(4):
            nx , ny = i + dx[k], j + dy[k]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#' and not visited[nx][ny]: 
                visited[nx][ny] = True
                queue.append([nx, ny])
    return sheep, wolf
    
sheep_tot, wolf_tot = 0, 0
for i in range(r):
    for j in range(c):
        if graph[i][j]:
            sheep, wolf = bfs(i, j)
            if sheep > wolf:
                sheep_tot += sheep
            else:
                wolf_tot += wolf
print(sheep_tot, wolf_tot)
            
'''
# 두번째 시도!!! 내가 맞췄다 답지 하나도 안보고!@#
import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
graph = [ list(input().rstrip()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    wolf, sheep = 0, 0
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft();
        if graph[x][y] == 'v':
            wolf += 1
        if graph[x][y] == 'k':
            sheep += 1
        graph[x][y] = '.'
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and graph[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append([nx, ny])
    if sheep > wolf:
        wolf = 0
    else:
        sheep = 0
    return sheep, wolf

t_sheep, t_wolf = 0, 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'v' or graph[i][j] == 'k':
            sheep, wolf = bfs(i, j)
            t_sheep += sheep
            t_wolf += wolf

print(t_sheep , t_wolf)

'''