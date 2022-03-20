'''
m개의 줄에 간선의 양 끝점 u, v

'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)
cnt = 0

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1
    
print(cnt)


''' 
두번째 풀이
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False for _ in range(N+1)]
    
def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)



bfs 사용
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)

def bfs(v):
    queue = deque([v]) 
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
cnt = 0
for i in range(1, n+1):
    if visited[i] == False:
        bfs(i)
        cnt += 1

print(cnt)
'''