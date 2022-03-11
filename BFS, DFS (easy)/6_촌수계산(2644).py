from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
x, y = map(int, input().split())
graph = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        # print('v : ' , v)
        for i in graph[v]:
            if not visited[i]:
                result[i] = result[v] + 1 # 왜 이렇게 되는지 잘은 모르겟다 ㅜㅜ
                queue.append(i)
                visited[i] = True
    
bfs(x)
# print(result)
print(result[y] if result[y] != 0 else -1)

'''
# 두번째 시도

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)] 
result = [0 for _ in range(n+1)]

for i in range(1, m+1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if not visited[i]:
                result[i] = result[x] + 1
                queue.append(i);
                visited[i] = True

bfs(start)
print(result[end] if result[end] != 0 else -1)


'''