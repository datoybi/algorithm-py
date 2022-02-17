from collections import deque

def bfs(S, T):
    q = deque()
    q.append((S, T, 0))
    check = [-1]*(200)
    while q:
        node, t, c = q.popleft()
        if node <= t and check[node] == -1:
            q.append((node*2, t+3, c+1))
            q.append((node+1, t, c+1))
            if node == t:
                return c

C = int(input())
for _ in range(C):
    S, T = map(int, input().split())
    print(bfs(S, T))