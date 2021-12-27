'''
맞았습니다! 
구현 조건만 맞으면 되는 구현문제 
'''
import sys
# 입력
A, B, N = list(), list(), int(sys.stdin.readline())

for i in range(N): # A SETTING
    A.append(int(sys.stdin.readline()))
for i in range(1, (N*2)+1): # B SETTING
    if i not in A:
        B.append(i)

A.sort(); B.sort()

# 연산
turn, now = 'A', 0

while True:
    if len(A) == 0 or len(B) == 0:
        break
    if now == 0: # 주어진 카드가 없으면
        if turn == 'A':
            now = A[0]
            del A[0]
            turn = 'B'
        else:
            now = B[0]
            del B[0]
            turn = 'A'
    else: # 주어진 카드가 있으면
        if turn == 'A': # A일때
            flag = False
            for i in range(len(A)):
                if A[i] > now: # 현재 카드보다 큰게 있다면
                    now = A[i]
                    del A[i]
                    flag = True
                    turn = 'B'
                    break
            if flag == False: # 없으면 상대방 첫번째 카드
                now = B[0]
                del B[0]
                turn = 'A'
        else: # B일때
            flag = False
            for i in range(len(B)):
                if B[i] > now:
                    now = B[i]
                    del B[i]
                    flag = True
                    turn = 'A'
                    break
            if flag == False:
                now = A[0]
                del A[0]
                turn = 'B'

print(len(B)); print(len(A))
