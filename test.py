from collections import deque
import sys
input = sys.stdin.readline

# dfs
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
# print(graph)    

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
print(graph) # [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
visited = [False] * (N+1)
print(visited)

def dfs(v):
    print(v)
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

print()