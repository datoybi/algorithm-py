'''
시뮬레이션? 일련의 명령에 따라서 개체를 차례대로 이동시키는 것

맞았습니다!

0 : 얼수도 있고 안얼수도 
0 > : 얼
0 < : 안얼 

원래 고기 온도 A    -100 <= A <= 100 (A != 0)
목표 온도 : B       1 <= B <= 100 (B < A)
얼어있는 고기를 1도 데우는데 걸리는 시간 C
얼어 있는 고기를 해동하는 데 걸리는 시간 D
얼어있지 않은 고기를 1도 데우는데 걸리는 시간 E

-10
20
5
10
3

120

''' 

'''
    만약 A가 음수이면 (0-A)*C + D + B*E
    A가 양수면 (B-A)*E
'''

import sys

A,B,C = int(sys.stdin.readline()), int(sys.stdin.readline()), int(sys.stdin.readline())
D, E, sum = int(sys.stdin.readline()), int(sys.stdin.readline()), 0

if A > 0:
    sum = (B-A)*E
else:

    sum = (0-A)*C + D + B*E

print(sum)