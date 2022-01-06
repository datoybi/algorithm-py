'''
N일
초기 현금 W
'''
import sys

n, W = list(map(int, sys.stdin.readline().split()))
lst = list()

for _ in range(n):
    lst.append(int(sys.stdin.readline()))    

for i in range(1, n):
    if lst[i-1] <= lst[i]:
       W += (lst[i] - lst[i-1]) * (W // lst[i-1])

print(W)