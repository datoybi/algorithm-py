'''
. 빈 필드 
# 울타리
o 양
v 늑대
수평 수직으로 이동가능
양> 늑대면 이기고 늑대 0
양 <늑대 양 0
'''

import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    sheep, wolf = 0, 0
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    while queue:
        r, c = queue.popleft()
        if graph[r][c] == 'o':
            sheep += 1
        elif graph[r][c] == 'v':
            wolf += 1
        graph[r][c] = '#' # 이게 중요.. 또 카운트 될 가능성 있음
        for i in range(4):
            nx = dx[i] + r
            ny = dy[i] + c
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != '#' and not visited[nx][ny]:
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
        if graph[i][j] == 'o' or graph[i][j] == 'v':
            sheep, wolf = bfs(i, j)
            t_sheep += sheep
            t_wolf += wolf

print(t_sheep, t_wolf)

    