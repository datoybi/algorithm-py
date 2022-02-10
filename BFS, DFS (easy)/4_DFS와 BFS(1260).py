# 맞았습니다!
from collections import deque

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited1 = [False] * (n+1)
visited2 = [False] * (n+1)
for i in range(len(graph)):
    graph[i].sort()

def dfs(graph, v, visited1):
    visited1[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited1[i]:
            dfs(graph, i, visited1)

def bfs(graph, v, visited2):
    queue = deque([v])
    visited2[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True

dfs(graph, k, visited1)
print()
bfs(graph, k, visited2)




