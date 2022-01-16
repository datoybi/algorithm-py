'''
맞았습니다!
프로젝트 팀 하나는 두명의 학생으로 구성 
학생수 : 2n이라 가정하자 (n은 양의 정수)
비등하게 하는데 작은수  
'''

import sys

int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
cnt = 987654321 

if len(lst) == 1:
    print(lst[0])
    exit(0)
for i in range(len(lst)//2):
    print(lst[0], lst[-1])
    cnt = min(cnt, lst[0] + lst[-1])
    del lst[0]; del lst[-1]
print(cnt)