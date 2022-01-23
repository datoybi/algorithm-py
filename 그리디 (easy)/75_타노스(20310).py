'''
맞았습니다!
0은 문자열 뒤부터 지워주고
1은 문자열 앞부터 지워준다
'''

import sys

S = list(sys.stdin.readline().rstrip())
zero = S.count('0')//2
one = S.count('1')//2

for _ in range(zero):
    S.pop(-S[::-1].index('0')-1) # 뒤부터 해당 원소 뺴낼 떄 사용 
    
for _ in range(one):
    S.pop(S.index('1'))
  
print(''.join(S))

