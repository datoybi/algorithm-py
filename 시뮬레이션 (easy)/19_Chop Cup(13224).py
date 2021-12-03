'''
맞았습니다!

공은 맨 왼쪽 컵 아래에서 시작

세가지 방법중 하나로 여러번 두 컵을 바꿈

AB 3
CBABCACCC 1

'''

import sys
change = sys.stdin.readline().rstrip()
ball = 1

for i in range(len(change)):
    if change[i] == 'A':
        if ball == 1:
            ball = 2
        elif ball == 2:
            ball = 1
    elif change[i] == 'B':
        if ball == 2:
            ball = 3
        elif ball == 3:
            ball = 2
    elif change[i] == 'C':
        if ball == 1:
            ball = 3
        elif ball == 3:
            ball = 1
    
print(ball)