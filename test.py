from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
link = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    # 선택한 노드부터 쭉 뻗어나갈 것이므로 링크를 반대로 달아준다.
    link[b].append(a)

maxLink,ans = 0,[]
for i in range(1,n+1):
    visited = [False]*(n+1)
    visited[i] = True
    q = deque([i])
    
    # BFS
    cnt = 0
    while q:
        v = q.popleft()
        for toNode in link[v]:
            if not visited[toNode]:
                visited[toNode] = True
                cnt += 1
                q.append(toNode)
    
    if cnt > maxLink:
        maxLink = cnt
        ans = [i]
    elif cnt == maxLink:
        ans.append(i)
print(*ans)