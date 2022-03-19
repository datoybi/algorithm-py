import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [-1] * (n+1)

def dfs(v):
    for i in graph[v]:
        if visited[i] == -1:
            visited[i] = v
            dfs(i)

dfs(1)
for i in range(2, n+1):
    print(visited[i])


'''
안보고 풀어서 맞췄다!! 뿌듯

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0 for _ in range(N+1)]
print(graph)

def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = x

for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)

for i in range(2, N+1):
    print(visited[i])

'''