'''
1
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
'''
import sys
from collections import deque
input = sys.stdin.readline

for i in range(int(input())):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(M)]
    
    for i in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1

    print(graph)
    