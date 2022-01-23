'''
맞았습니다!

n개의 퀘스트, n개의 아케인스톤, 5억 이상의 경험치 
최대 k개의 아케인스톤이 동시에 활성화
n, k (1 <= k <= n <= 300000)
n개의 정수
'''
import sys

N, K = list(map(int, sys.stdin.readline().split()))
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
cnt, ans = 1, 0

for i in range(1, len(lst)):
    ans += lst[i] * cnt
    if cnt < K:
        cnt += 1 

print(ans)