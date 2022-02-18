import sys
input = sys.stdin.readline
n = int(input())
graph = [[0, 0, 0] for _ in range(n+1)]
for i in range(1, n+1):
    s, e, c = map(int, input().split())
    graph[i] = [s, e, c]
print(graph)

def dfs(v):
    tmp = []
    for i in range(1, n+1):
        if graph[v][1] <= graph[i][0]:
            tmp.append(i)    
    
    print(tmp)
