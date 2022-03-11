# 왜 매 순회마다 visited를 초기화 해야 할까??
# 어렵다 다음에 또 해보기.. 
# 왜 매 순회마다 visited 초기화 하는지 알아냈다!@#

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

'''
두번째 시도 
import sys
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


'''