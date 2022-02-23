'''
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
'''
from collections import deque
import sys
input = sys.stdin.readline

# tc
M, N, K = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]
print(graph)

for i in range(K):
    a, b = map(int, input().split())
    graph[a][b] = 1

print(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < 


