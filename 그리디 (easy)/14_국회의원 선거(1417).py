'''
맞았습니다!

국회의원 후보 N, 주민 M명
다솜이는 기호 1번, 다른 모든 사람의 득표수보다 많은 득표수 
후보의 수 N
N줄에 걸쳐 뽑으려는 득표수가 나옴맞! 
'''

import sys

# 입력
lst = []
for i in range(int(sys.stdin.readline())):
    lst.append(int(sys.stdin.readline()))
# 길이가 1인경우 처리
if len(lst) == 1: 
    print(0)
    exit(0)
dasom = lst[0]; del lst[0]
cnt = 0

while True:
    if dasom > max(lst):
        break
    idx = lst.index(max(lst))
    lst[idx] -= 1
    dasom += 1
    cnt += 1

print(cnt)