'''
앞으로 디버깅 좀 돌려보고 하기
'''
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
s, e = map(int, input().split())
teleport = [[] for _ in range(n+1)]
result = [-1 for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    teleport[a].append(b)
    teleport[b].append(a)

def bfs(v):
    queue = deque([v])
    result[v] = 0 # 왜 이렇게 하는지 모르겟다
    while queue:
        x = queue.popleft()
        tmp = [x-1, x+1] # 양 옆으로 갈 수 있는 경우의 수 추가
        if teleport[x]:
            tmp += teleport[x] # 텔레포트로 갈수있는 경우의 수 추가
        for i in tmp: # 가능한 경우의 수 순회
            if (1 <= i <= n) and result[i] == -1:
                queue.append(i)
                result[i] = result[x] + 1
            if i == e:
                return result[i]

cnt = bfs(s)
print(cnt)
