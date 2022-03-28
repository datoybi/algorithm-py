import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    graph = [int(input()) for _ in range(N)]
    graph.insert(0, 0)
    result = [0 for _ in range(N+1)]

    def dfs(v):
        i = graph[v]
        if result[i] == 0:
            result[i] = result[v] + 1
            dfs(i)

    dfs(1)
    print(result[N])

