'''
. 빈 필드 
# 울타리
o 양
v 늑대
수평 수직으로 이동가능
양> 늑대면 이기고 늑대 0
양 <늑대 양 0
'''
import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
graph = [[] for _ in range(R+1)]
print(graph)

for i in range(1, R+1):
    a = input().rstrip()
    graph[i] = a

print(graph)
print(graph[1][1])
    