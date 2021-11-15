'''
 (1 ≤ N ≤ M ≤ 5000)

87 104
14
989 1022
0
22 25
3
1234 1234
1

'''
import sys

N,M = map(int, sys.stdin.readline().split())

for i in range(N, M+1):
    tmp = list(str(i))
    print(tmp)
    # for j in range(len(tmp)):
    #     # print(tmp[j])
    #     if tmp[j] not in tmp:
    #         print(tmp)

