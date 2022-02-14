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
            


