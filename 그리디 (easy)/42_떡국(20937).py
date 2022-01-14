
import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

print(lst)
lst.sort()
print(lst)
cnt = 0
num = lst[0]
for i in range(1, len(lst)):
    print(lst)
    if num+1 not in lst:
        cnt += 1
        num += 1
    elif num+1 in lst:
        del lst[lst.index(num+1)]
        
print(cnt)