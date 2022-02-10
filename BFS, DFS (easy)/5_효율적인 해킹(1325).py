import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    # graph[a].append(b) # 둘을 쓰면 양방향 연결이고 단반향 연결은 하나만 쓰면됨
print(graph)

visited = [0] * (n+1)

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            queue.append(i)

answer = [0 for _ in range(n+1)]
for i in range(1, n):
    answer[i] = bfs(i)   
# dfs(1)
# print('cnt : ' , cnt)             
