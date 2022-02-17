from collections import deque
import sys

def bfs(node):
    q = deque()
    q.append(node)
    check[node] = 0
    while q:
        node = q.popleft()
        d = [node-1, node+1]
        if graph[node]:
            d += graph[node]
            print(d)
        for n in d:
            if (1 <= n <= N) and check[n] == -1:
                q.append(n)
                check[n] = check[node]+1
            if n == E:
                return check[n]

N, M = map(int, sys.stdin.readline().split())
S, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
check = [-1]*(N+1)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)
print(check)

cnt = bfs(S)
print(cnt)