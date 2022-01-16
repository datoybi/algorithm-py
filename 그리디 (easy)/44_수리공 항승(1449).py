import sys

N, L = list(map(int, sys.stdin.readline().split()))
lst = list(map(int, sys.stdin.readline().split()))
tape, cnt = list(), 0
lst.sort()

for i in range(N):
    if lst[i] not in tape:
        cnt += 1
        for j in range(lst[i], lst[i]+L):
            tape.append(j)     
print(cnt)

