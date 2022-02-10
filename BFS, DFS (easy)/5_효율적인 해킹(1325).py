n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)
print(graph)
visited = [0] * (n+1)
cnt = 0

def dfs(v):
    global cnt
    visited[v] = 1
    print(v)
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1
            print('yes' , i)
    
dfs(1)
print('cnt : ' , cnt)             
print(visited)