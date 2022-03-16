# bfs 사용
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    graph[x][y] = 0
    queue = deque()
    queue.append([x, y])
    while queue:
        print(queue)
        i, j = queue.popleft()
        for k in range(8):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    graph = [list(map(int, input().split())) for _ in range(m)]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)



'''
# 두번째 시도

import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    graph[x][y] = 0
    queue = deque()
    queue.append([x, y])
    while queue:
        i, j = queue.popleft()
        for k in range(8):
            nx, ny = dx[k] + i, dy[k] + j
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0 : break;
    graph = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)




dfs 사용
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    graph[x][y] = 0
    for k in range(8):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
            dfs(nx, ny)

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    graph = [list(map(int, input().split())) for _ in range(m)]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)
'''