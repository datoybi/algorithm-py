'''
맞았습니다!
마일리지 과목당 1~36
과목에 대해서 마일리지를 많이 투자한 순으로 그 과목의 수강인원만큼 신청되는 방식
마일리지는 한 과목에 1에서 36까지 넣을 수 있다.

'''
import sys

n, m = list(map(int, sys.stdin.readline().split()))
result = list()
for i in range(n):
    p, l = list(map(int, sys.stdin.readline().split())) #  신청한 사람, 가용 인원
    lst = list(map(int, sys.stdin.readline().split()))
    lst.sort(reverse=True)
    
    if p >= l:
        result.append(lst[l-1])
    else:
        result.append(1)
result.sort()

cnt = 0
for i in range(1,len(result)+1):
    if sum(result[0:i]) > m:
        break
    else:
        cnt += 1

print(cnt)