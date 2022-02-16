from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        print(queue)
        i, j = queue.popleft()
        for k in range(8):
            nx, ny = i + dx[k], j + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0: # 0이면
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y]+1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)

max_val = 0
for i in range(n):
    max_val = max(max_val, max(graph[i]))
print(max_val)