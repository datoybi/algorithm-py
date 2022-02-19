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
print(cnt)