# 와우! 답지 안보고 내가 풀었뜸!@#
from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
result = [0] * (N+1)
visited = [False] * (N+1)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                result[i] = result[x] + 1
                visited[i] = True

bfs(X)
flag = False
for i in range(1, N+1):
    if K == result[i]:
        print(i)
        flag = True

if flag == False:
    print(-1) 

'''
두번째 시도
import sys
input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
result = [-1 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(v):
    queue = deque([v])
    result[v] = 0
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if result[i] == -1:
                queue.append(i)
                result[i] = result[x] + 1

bfs(X)
flag = False
for i in range(1, N+1):
    if result[i] == K:
        print(i)
        flag = True

if flag == False: print(-1);

'''