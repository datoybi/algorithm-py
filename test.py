import sys
input = sys.stdin.readline

def dfs(k, graph):
    print(graph)
    graph[k] = -2
    for i in range(n):
        if graph[i] == k:
            dfs(i, graph)

n = int(input())
graph = list(map(int, input().split()))
k = int(input())

dfs(k, graph)
cnt = 0
for i in range(len(graph)):
    if graph[i] != -2 and i not in graph:
        cnt += 1
print(cnt)