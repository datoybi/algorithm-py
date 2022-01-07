'''
맞았습니다!
책의 개수 N (0 <= N <= 50)
최대 무게 M (M <= 1000) 
책의 무게는 M보다 작거나 같은 자연수
'''
import sys

N, M = list(map(int, sys.stdin.readline().split()))
if N == 0: 
    print(0)
    exit(0)
lst = list(map(int, sys.stdin.readline().split()))
cnt = 1
weight = lst.pop()

for i in range(len(lst)):
    if weight < M:
        if weight + lst[-1] > M:
            cnt += 1
            weight = lst.pop()
        else:
            weight += lst.pop()
    elif weight == M:
        cnt += 1
        weight = lst.pop()

print(cnt)