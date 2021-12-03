

import sys

lst = [i for i in range(1, 21)]

for _ in range(10):
    n, m =  list(map(int, sys.stdin.readline().split()))
    # for i in range(n):
    tmp = lst[n-1:m]
    for i in range(n,m+1): # 삭제하고
        # print(lst[n-1])
        del lst[n-1]
    for i in range(len(tmp)): # 넣기
        lst.insert(n-1, tmp[i])

for i in lst:
    print(i, end =' ')
