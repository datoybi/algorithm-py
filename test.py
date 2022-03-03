import sys
input = sys.stdin.readline


N, M, V = map(int, input().split())
print(N, M, V)
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

for i in range(1, N+1):
    graph[i].sort(key = lambda x : x)

print(graph)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for i in range(1, N+1):
    if visited[i] == False:
        dfs(i)

# dfs(1)



'''

N 정점의 개수
M 간선의 개수
V 탐색을 시작할 번호

4 5 1
1 2
1 3
1 4
2 4
3 4

1 2 4 3
1 2 3 4


5 5 3
5 4
5 2
1 2
3 4
3 1
'''