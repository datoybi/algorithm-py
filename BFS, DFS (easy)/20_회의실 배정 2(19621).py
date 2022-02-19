# 풀다 만.. 무슨 말인지 모르겟..담에 또 풀어보자 ㅠ

import sys
input = sys.stdin.readline
n = int(input())
graph = [[0, 0, 0] for _ in range(n+1)]
for i in range(1, n+1):
    s, e, c = map(int, input().split())
    graph[i] = [s, e, c]
print(graph)
result = [0]* (n+1)
print(result)
visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    print(result)
    for i in range(1, n+1):
        if not visited[i] and graph[v][1] <= graph[i][0]:
            result[i] += graph[i][2] + result[v]
            dfs(i)

for i in range(1, n+1):
    result[i] = graph[i][2]
    dfs(i)

print(result)


'''

from sys import stdin 
input = stdin.readline 

def dfs(n, val): 
    global res 
    if n >= N and res < val: 
        res = val 
        return 

    for i in range(n, N): 
        dfs(i+2, val+arr[i][2]) 

N = int(input()) 
arr = [tuple(map(int, input().split())) for i in range(N)] 
arr.sort() 
res = 0 
dfs(0, 0) 
print(res)
'''