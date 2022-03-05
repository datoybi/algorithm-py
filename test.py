import sy
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph =[[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(v):
    global cnt
    cnt += 1
    visited[v] = True
    queue = deque([v])
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt += 1    
    return cnt

lst = list()
for i in range(1, N+1):
    cnt = 0
    visited = [False] * (N+1)
    lst.append(bfs(i))

max_val = max(lst)
for i in range(N):
    if max_val == lst[i]:
        print(i+1, end=' ')
