import sys
input = sys.stdin.readline
from collections import deque

dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

def bfs(sx, sy, ax, ay):
    graph[sx][sy] = 1
    queue = deque()
    queue.append([sx, sy])
    while queue:
        a, b = queue.popleft()
        if a == ax and b == ay:
            print(graph[ax][ay]-1) # 알쏭달쏭
            return
        for k in range(8):
            nx, ny = dx[k] + a, dy[k] + b
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                queue.append([nx, ny])
                graph[nx][ny] = graph[a][b] + 1 # 알쏭달쏭

for _ in range(int(input())):
    n = int(input())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    sx, sy = map(int, input().split()) # 시작 지점
    ax, ay = map(int, input().split()) # 도착 지점 
    bfs(sx, sy, ax, ay)    
    
    

