'''
어떻게 풀어야 하는지 감도 안온다 .. 


'''

import sys

lst = list()
n = 0
for _ in range(int(sys.stdin.readline())):
    lst.append(int(sys.stdin.readline()))
print(lst)
for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        n = i+1
print(lst[n])
