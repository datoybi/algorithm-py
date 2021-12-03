'''
    보드는 N칸
    출발점 1칸, 도착점 N칸
    주사위를 굴려서 도착한 곳에 지시사항을 1번 따른다
    N에 도달하면 도착

    N, M 주사위 던진 횟수 (2 <= N <= 1000, 1 <= M <= 1000)
    N개 줄은 -999 <= N <= 999

    1번 칸과 N번 칸에 쓰여 있는 지시사항은 항상 0
    항상 주사위를 M번 이하로 던져서 도착할 수 있다.
    1보다 작은 칸으로 이동하라는 지시가 있는 경우도 없다.


 ? 도착을 못하는 경우는 없나보다
'''
# 이건 맞는다.. 이렇게해야 맞다 왜냐면 처음에는 now는 1일 것이고 시뮬에 맞게 구현한게 이게 맞다
import sys

N, M = list(map(int, sys.stdin.readline().split()))
board = [0] + [int(input()) for _ in range(N)]
dice = [0] + [int(input()) for _ in range(M)]

now = 1
for i in range(1, M+1):
    now += dice[i] 
    if now >= N: # 현재 위치가 N과 같으면
        print(i)
        break

    now += board[now]
    if now >= N: # N보다 현재위치가 같거나 크면 
        print(i)
        break



# 이건 틀렸는데
import sys

N, M = list(map(int, sys.stdin.readline().split()))
dice, board = list(), list()
board.append(0)
dice.append(0)

for i in range(N):
    board.append(int(sys.stdin.readline()))

for i in range(M):
    dice.append(int(sys.stdin.readline()))

now = 1
for i in range(1, M+1):
    if now >= N: # 현재 위치가 N과 같으면
        print(i)
        break
    now += dice[i]

    if now >= N: # N보다 현재위치가 같거나 크면 
        print(i)
        break
    now += board[now]
