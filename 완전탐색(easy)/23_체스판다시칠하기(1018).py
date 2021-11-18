'''
맞았습니다!
'''
N,M = map(int, input().split())
board, count = list(), list()

for _ in range(0,N):
    board.append(list(input()))

for n in range(0, N-7):
    for m in range(0, M-7):
        cnt1, cnt2 = 0, 0
        for column in range(n, n+8):
            if column % 2 == 0: 
                flag1, flag2 = 'W', 'B'
            else:
                flag1, flag2 = 'B', 'W'
                
            for row in range(m, m+8):
                if board[column][row] != flag1:
                    cnt1 += 1
                if board[column][row] != flag2:
                    cnt2 += 1

                if flag1 == 'W':
                    flag1 = 'B'
                else:
                    flag1 = 'W'

                if flag2 == 'W':
                    flag2 = 'B'
                else:
                    flag2 = 'W'
 

        count.append(cnt1)
        count.append(cnt2)


print(min(count))

