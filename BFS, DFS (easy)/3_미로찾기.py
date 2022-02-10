
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 1:
            graph[x][y] += 1
            bfs(x - 1, y)
            bfs(x, y - 1)
            bfs(x + 1, y)
            bfs(x, y + 1)
            return True
        return False

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        bfs(i, j)

print(graph)           