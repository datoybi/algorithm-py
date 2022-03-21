'''
queue를 한번에 넣는것과 그렇지 않은것의 차이는 뭘까...........
거기까지 생각이 미치지 못하였다....ㅠ
'''
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
queue = deque()

def bfs():
    while queue:
        print(queue)
        i, j = queue.popleft()
        for k in range(8):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[i][j] + 1
                queue.append([nx, ny])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])
bfs()

max_val = 0
for i in range(n):
    max_val = max(max_val, max(graph[i]))
print(max_val-1)


'''
두번쨰 시도 (혼자서 못 풀음.. 알듯 말듯..)
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
print(graph)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
queue = deque()

def bfs():
    while queue:
        a, b = queue.popleft()
        for i in range(8):
            nx, ny = dx[i] + a, dy[i] + b
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                queue.append([nx, ny])
                print('!' , a, b, nx, ny)
                graph[nx][ny] = graph[a][b] + 1

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
                queue.append([i, j])

bfs()
max_val = 0
for i in range(N):
    max_val = max(max_val,max(graph[i]))

print(max_val-1)    


from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
print(graph)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
# result = [[0 for _ in range(m)] for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    print(queue)
    while queue:
        i, j = queue.popleft()
        for k in range(8):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[i][j] + 1
                queue.append([nx, ny])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)

print(graph)



한꺼번에 넣엇을 때
deque([[0, 2], [2, 0], [4, 3]])
deque([[2, 0], [4, 3], [0, 1], [0, 3], [1, 1], [1, 2], [1, 3]])
deque([[4, 3], [0, 1], [0, 3], [1, 1], [1, 2], [1, 3], [1, 0], [2, 1], [3, 0], [3, 1]])
deque([[0, 1], [0, 3], [1, 1], [1, 2], [1, 3], [1, 0], [2, 1], [3, 0], [3, 1], [3, 2], [3, 3], [4, 2]])
deque([[0, 3], [1, 1], [1, 2], [1, 3], [1, 0], [2, 1], [3, 0], [3, 1], [3, 2], [3, 3], [4, 2], [0, 0]])
deque([[1, 1], [1, 2], [1, 3], [1, 0], [2, 1], [3, 0], [3, 1], [3, 2], [3, 3], [4, 2], [0, 0]])
deque([[1, 2], [1, 3], [1, 0], [2, 1], [3, 0], [3, 1], [3, 2], [3, 3], [4, 2], [0, 0], [2, 2]])
deque([[1, 3], [1, 0], [2, 1], [3, 0], [3, 1], [3, 2], [3, 3], [4, 2], [0, 0], [2, 2], [2, 3]])
deque([[1, 0], [2, 1], [3, 0], [3, 1], [3, 2], [3, 3], [4, 2], [0, 0], [2, 2], [2, 3]])
deque([[2, 1], [3, 0], [3, 1], [3, 2], [3, 3], [4, 2], [0, 0], [2, 2], [2, 3]])
deque([[3, 0], [3, 1], [3, 2], [3, 3], [4, 2], [0, 0], [2, 2], [2, 3]])
deque([[3, 1], [3, 2], [3, 3], [4, 2], [0, 0], [2, 2], [2, 3], [4, 0], [4, 1]])
deque([[3, 2], [3, 3], [4, 2], [0, 0], [2, 2], [2, 3], [4, 0], [4, 1]])
deque([[3, 3], [4, 2], [0, 0], [2, 2], [2, 3], [4, 0], [4, 1]])
deque([[4, 2], [0, 0], [2, 2], [2, 3], [4, 0], [4, 1]])
deque([[0, 0], [2, 2], [2, 3], [4, 0], [4, 1]])
deque([[2, 2], [2, 3], [4, 0], [4, 1]])
deque([[2, 3], [4, 0], [4, 1]])
deque([[4, 0], [4, 1]])
deque([[4, 1]])

아닐떄
deque([[0, 2]])
deque([[0, 1], [0, 3], [1, 1], [1, 2], [1, 3]])
deque([[0, 3], [1, 1], [1, 2], [1, 3], [0, 0], [1, 0]])
deque([[1, 1], [1, 2], [1, 3], [0, 0], [1, 0]])
deque([[1, 2], [1, 3], [0, 0], [1, 0], [2, 1], [2, 2]])
deque([[1, 3], [0, 0], [1, 0], [2, 1], [2, 2], [2, 3]])
deque([[0, 0], [1, 0], [2, 1], [2, 2], [2, 3]])
deque([[1, 0], [2, 1], [2, 2], [2, 3]])
deque([[2, 1], [2, 2], [2, 3]])
deque([[2, 2], [2, 3], [3, 0], [3, 1], [3, 2]])
deque([[2, 3], [3, 0], [3, 1], [3, 2], [3, 3]])
deque([[3, 0], [3, 1], [3, 2], [3, 3]])
deque([[3, 1], [3, 2], [3, 3], [4, 0], [4, 1]])
deque([[3, 2], [3, 3], [4, 0], [4, 1], [4, 2]])
deque([[3, 3], [4, 0], [4, 1], [4, 2]])
deque([[4, 0], [4, 1], [4, 2]])
deque([[4, 1], [4, 2]])
deque([[4, 2]])
deque([[2, 0]])
deque([[4, 3]])
'''
