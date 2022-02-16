from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dx = (-1, -1, -1, 0, 0, 1, 1, 1)
dy = (-1, 0, 1, -1, 1, -1, 0, 1)
q = deque()

def bfs():
    while q:
        print(q)
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x+dx[k], y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if a[nx][ny] == 0: # 0이면
                # print(nx, ny)
                q.append((nx, ny))
                a[nx][ny] = a[x][y]+1

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            q.append((i, j))
bfs()
print(max(map(max, a))-1)
print(a)


'''
1 3
1 0 0
'''