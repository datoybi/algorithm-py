# 어우 여려워..
import sys
from collections import deque
input = sys.stdin.readline
r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    sheep, wolf = 0, 0
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 'v':
            wolf += 1
        if graph[x][y] == 'o':
            sheep += 1
        graph[x][y] = '#'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])
    if sheep > wolf:
        wolf = 0
    else:
        sheep = 0
    return sheep, wolf

tot_sheep, tot_wolf = 0, 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'o' or graph[i][j] == 'v':
            sheep, wolf = bfs(i, j)
            tot_sheep += sheep
            tot_wolf += wolf

print(tot_sheep, tot_wolf)



'''
r,c=map(int,input().split())
g=[[{'#': 0,
    '.':1,
    'o':2,
    'v':3
    }[j]for j in input()]for i in[0]*r]
def f(i,j):
    q=[(i,j)]
    x,y=0,0
    while q:
        i, j=q.pop()
        if g[i][j]==2:
            x+=1
        elif g[i][j]==3:
            y+=1
        g[i][j]=0
        for i,j in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if i>-1 and i<r and j>-1 and j<c and g[i][j]:q+=[[i,j]]
    return x, y
x, y = 0, 0
for i in range(r):
    for j in range(c):
        if g[i][j]:
            v, w = f(i,j)
            if v > w:
                x += v
            else:
                y += w
print(x,y)
'''