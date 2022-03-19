# 맞았습니다!
# 자꾸 메모리 초과 남 ㅜㅜ 
# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline
# n, m = map(int, input().split())
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# board = [list(map(int, list(input().rstrip()))) for _ in range(n)]

# def dfs(x, y):
#     board[x][y] = -1
#     for i in range(4):
#         nx, ny = dx[i] + x, dy[i] + y
#         if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
#             dfs(nx, ny)

# for i in range(m):
#     if board[0][i] == 0:
#         dfs(0, i)

# if -1 in board[-1]:
#     print('YES')
# else:
#     print('NO')


# bfs로 해결 
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                queue.append([nx, ny])
                board[nx][ny] = -1

for i in range(m):
    if board[0][i] == 0:
        bfs(0, i)

if -1 in board[-1]:
    print('YES')
else:
    print('NO')


'''
두번째 시도 -> 맞췃당 게다가 훨씬 간결한듯
import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(M)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    queue = deque();
    queue.append([x, y])
    graph[x][y] = '2'
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + a, dy[i] + b
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == '0':
                queue.append([nx, ny])
                graph[nx][ny] = '2'

for i in range(N):
    if graph[0][i] == '0':
        bfs(0, i)

print('YES' if '2' in graph[M-1] else 'NO')

'''