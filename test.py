import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = list(map(int, input().split()))
graph.insert(0, 0)
s = int(input())
# print(graph)
visited = [False for _ in range(n+1)]

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in [-graph[x], graph[x]]:
            tmp = x + i
            if 0 <= tmp <= n and not visited[tmp]:
                queue.append(tmp)
                visited[tmp] = True
                            
bfs(s)
print(visited)
print(visited[1:].count(True))
