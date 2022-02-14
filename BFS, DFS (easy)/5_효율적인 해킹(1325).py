# 왜 매 순회마다 visited를 초기화 해야 할까??
# 어렵다 다음에 또 해보기.. 

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    # graph[a].append(b) # 둘을 쓰면 양방향 연결이고 단반향 연결은 하나만 쓰면됨
        
max_val, answer = 0, []
for i in range(1, n+1):
    cnt = 0
    visited = [False] * (n+1)
    visited[i] = True
    queue = deque([i])

    while queue:
        x = queue.popleft()
        for j in graph[x]:
            if not visited[j]:
                visited[j] = True
                cnt += 1
                queue.append(j)

    if cnt > max_val:
        max_val = cnt
        answer = [i]
    elif cnt == max_val:
        answer.append(i)
print(*answer)
