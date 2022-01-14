'''
맞았습니다! (O(n))
와씨 천재다,, 중복값이 있으면 무조건  count + 1 이다
4
1 1 1 1
4

12
1 2 3 4 1 2 3 4 1 2 3 4
3

5
4 2 3 1 2
2
'''

import sys
zero_lst = [0 for _  in range(500001)]
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

for i in range(len(lst)):
    zero_lst[lst[i]] += 1

print(max(zero_lst))