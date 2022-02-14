'''

5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0

'''

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