'''
맞았습니다!
정답 보고 맞추고 내가 따라 쳐봤다.
'''
n = int(input()); m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False for _ in range(n+1)] 
cnt = 0

def dfs(start):
    global cnt
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)