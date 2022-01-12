'''
맞았습니다!
'''

import sys
A, B = list(map(int, sys.stdin.readline().split()))
favorite = list()
for _ in range(int(sys.stdin.readline())):
    favorite.append(int(sys.stdin.readline()))

lst = list()
min_val = 1000
for i in range(len(favorite)):
    min_val = min(min_val, abs(B - favorite[i]))

if min_val >= abs(B-A):
    print(abs(B-A))
else:  
    print(min_val+1)