import sys
input = sys.stdin.readline
from collections import deque

dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

def bfs(sx, sy, ex, ey):
    graph[sx][sy] = 1
    queue = deque()
    queue.append([sx, sy])
    
    while queue:
        a, b = queue.popleft()
        if a == ex and b == ey:
            print(graph[ex][ey]-1) # 알쏭달쏭
            return
        for i in range(8):
            nx, ny = dx[i] + a, dy[i] + b
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                queue.append([nx, ny])
                graph[nx][ny] = graph[a][b] + 1 # 알쏭달쏭
                
for _ in range(int(input())):
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    bfs(sx, sy, ex, ey)
