import sys
input = sys.stdin.readline
from collections import deque

dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

i = int(input())
graph = [[0 for _ in range(i)] for _ in range(i)]
print(graph)

# print(visited)
start_x, start_y = map(int, input().split())
end_x, end_y = map(int, input().split())

def bfs(x, y):
    cnt = 999999999
    total = 0
    visited = [[False for _ in range(i)] for _ in range(i)]
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        print(x, y, total)
        if x == end_x and y == end_y:
            cnt = min(cnt, total)
            print(cnt)
        total += 1
        for k in range(8):
            nx, ny = dx[k] + x, dy[k] + y
            if 0 <= nx < i and 0 <= ny < i and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])
           
                # 여기 넣은거 어캐 다 뺴지?

bfs(start_x, start_y)

























'''

8
0 0
7 0
'''