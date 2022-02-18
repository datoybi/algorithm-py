'''
1
7
2
3
4
5
6
7
1
'''
import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    graph = [0] * (n+1)
    for i in range(1, n+1):
        graph[i] = int(input())
    result = [0] * (n+1)

    def dfs(v):
        i = graph[v]
        if result[i] == 0:
            result[i] = result[v] + 1
            dfs(i)

    dfs(1)
    print(result[n])
