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
