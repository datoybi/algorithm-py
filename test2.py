import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append([x, y, 0])
    check = [-1] * 200 # 왜 200??????? 100이면 런타임 에러...
    while queue:
        i, j, cnt = queue.popleft()
        if i <= j and check[i] == -1:
            queue.append([i*2, j+3, cnt+1])
            queue.append([i+1, j, cnt+1])
            if i == j:
                return cnt

for _ in range(int(input())):
    S, T = map(int, input().split())
    print(bfs(S, T))
