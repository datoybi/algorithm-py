# 비슷한 문제를 DP에서 본적이 있는 것 같다 이 문제가 왜 그래프 탐색으로 구현을 해야할까 DP가 아니라..?! 아직 모르겠담
from collections import deque

def bfs(S, T):
    queue = deque()
    queue.append((S, T, 0))
    check = [-1] * 200
    while queue:
        node, t, c = queue.popleft()
        if node <= t and check[node] == -1:
            queue.append((node*2, t+3, c+1))
            queue.append((node+1, t, c+1))
            if node == t:
                return c

C = int(input())
for _ in range(C):
    S, T = map(int, input().split())
    print(bfs(S, T))

'''
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append([x, y, 0])
    check = [-1] * 200 # 왜 200??????? 100이면 런타임 에러...B가 200점 이상이 되는 최단경로는 없으니까
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



'''