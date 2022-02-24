'''
어떤 사람 A가 또다른 사람 B의 2-친구가 되려면
1. 두 사람이 친구
2. A와 친구이고 B와 친구인 C가 존재해야 한다.

가장 유명한 사람은 2-친구의 수가 가장 많은 사람 

'''
import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
d = int(input())
print(lst)

def dfs(num, lst):
    lst[num] = -2
    for i in range(len(lst)):
        if num == lst[i]:
            dfs(i, lst)

dfs(d, lst)
cnt = 0
for i in range(len(lst)):
    if lst[i] != -2 and i not in lst:
        cnt += 1
print(cnt)# d.

