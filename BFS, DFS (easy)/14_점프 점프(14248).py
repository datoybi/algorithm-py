# 어렵..
from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        x = queue.popleft()
        for i in [-graph[x], graph[x]]: 
            t = x + i # 이게 왜 나올까??
            if 0 <= t < n and visited[t] == 0:
                queue.append(t)
                visited[t] = 1

n = int(input())
visited = [0]* n
graph = list(map(int, input().split()))
s = int(input())-1
bfs(s)
print(visited.count(1))