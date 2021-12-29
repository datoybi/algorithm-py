'''
맞았습니다!
슥삭슥삭 연필로 규칙 찾다가
둘의 큰 차 = 중간값 - 1
이라는 규칙을 찾아내서 쉽게 풀었담
'''

# import sys

# while True:
#     try:
#         A, B, C = list(map(int, sys.stdin.readline().split())) 
#         dff = B-A if B-A > C-B else C-B
#         print(dff-1)
#     except:
#         break

import sys

while True:
    try:
        A, B, C = list(map(int, sys.stdin.readline().split())) 
        print(max(B-A, C-B)-1)
    except:
        break